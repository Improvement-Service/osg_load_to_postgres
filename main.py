import argparse
from operator import itemgetter
import utils
import ftp_helpers
from sdtf_processing import SdtfProcessing
import time

# def get_input_arg():
#     #Variables from command line
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-t', '--type', choices=['a', 'e'], help='sdtf file type: (choose from:  a, e)', required=True)
#     args = parser.parse_args()
#     return args.type.upper()


def main():


    #### CONFIG ####
    # SDTF file type to process
    sdtf_type = utils.get_input_arg()
    print(sdtf_type)


    # Configuration - see config.yml. Follow structure in config-example.yml
    conf = utils.get_config('./config.yml', sdtf_type)
    
    in_dir = conf['directories']['in']
   


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

    # ### Temp values for split testing
    # download_file = 'in/9080_20210715_A_04.zip'

    ### DATA PREP ###
    # Create child folder, unzip and split file into component tables
    print(download_file)
    sdtf_file = SdtfProcessing(download_file)
    sdtf_file.unzip_sdtf()
    sdtf_file.create_folder()
    sdtf_file.split_by_record_id()
    #sdtf_file.clean_up()

        # DB Config
    db, live_schema, tmp_schema, user, host, port = itemgetter('db', 'schema', 'tmp_schema', 'user', 'host', 'port')(conf['pg'])
    #osg_db = sdtf2pg.OsgPsqlDbLoad(db, live_schema, temp_schema, user, sdtf_type, host, port)
    data_dir = sdtf_file.temp_dir

    # Create 
    osg_db.create_temp_schema()
    osg_db.psql_create_tables()
    osg_db.psql_load_data(data_dir)
    osg_db.psql_add_geom()
    osg_db.move_temp_to_live()


    # cleanup


if __name__ == '__main__':
    main()
