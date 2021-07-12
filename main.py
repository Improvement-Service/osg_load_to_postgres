import argparse
from operator import itemgetter
import utils
import ftp_helpers

def get_input_arg():
    #Variables from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', choices=['a', 'e'], help='sdtf file type: (choose from:  a, e)', required=True)
    args = parser.parse_args()
    return args.type.upper()


def main():


    #### CONFIG ####
    # SDTF file type to process
    sdtf_type = get_input_arg()
    print(sdtf_type)


    # Configuration - see config.yml. Follow structure in config-example.yml
    conf = utils.get_config('./config.yml')
    
    in_dir = conf['directories']['in']
   
    # DB Config
    host, port, db, user = itemgetter('host', 'port', 'db', 'user')(conf['pg'])
    # User config in function then delete afterwards
    print(host, port, db, user)
    del host, port, db, user


    #### FTP DOWNLOAD ####
    # Connect to the FTP site and download the most recent file of right SDTF type.
    # API config
    host, port, user, passwd = itemgetter('host', 'port', 'user', 'passwd')(conf['api'])
    print(host, port, user, passwd)
    # FTP object
    osgftp = ftp_helpers.DownloadNationalExtract(host, port, user, passwd)
    osgftp.establish_secure_connection()
    latest_file = osgftp.identify_most_recent_file(sdtf_type)
    download_file = osgftp.download_most_recent_file(latest_file, 'in')

    ### DATA PREP ###
    # Create child folder, unzip and split file into component tables
    print(download_file)
    unzipped_files = utils.Utils.unzip_file(download_file, in_dir)
    for f in unzipped_files:
        utils.Utils.create_child_folder(f)





if __name__ == '__main__':
    main()
