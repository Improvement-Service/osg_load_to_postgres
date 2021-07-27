import argparse
from operator import itemgetter
import utils
import ftp_helpers
from sdtf_processing import SdtfProcessing
from sdtf2pg import OsgPsqlDbLoad
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
    
    in_dir = conf['directories']['data_in']
   


    # #### FTP DOWNLOAD ####
    # # Connect to the FTP site and download the most recent file of right SDTF type.
    # # API config
    # host, port, user, passwd = itemgetter('host', 'port', 'user', 'passwd')(conf['api'])
    # print(host, port, user, passwd)
    # # FTP object
    # osgftp = ftp_helpers.DownloadNationalExtract(host, port, user, passwd)
    # osgftp.establish_secure_connection()
    # latest_file = osgftp.identify_most_recent_file(sdtf_type)
    # download_file = osgftp.download_most_recent_file(latest_file, in_dir)

    # # ### Temp values for split testing
    # # download_file = 'in/9080_20210715_A_04.zip'

    # ### DATA PREP ###
    # # Create child folder, unzip and split file into component tables
    # print(download_file)
    # sdtf_file = SdtfProcessing(download_file)
    # sdtf_file.unzip_sdtf()
    # sdtf_file.create_folder()
    # sdtf_file.split_by_record_id()
    # #sdtf_file.clean_up()


    ### Prep for DB load ###
    #data_dir = sdtf_file.temp_dir
    data_dir = 'data_in/9080_20210727_E_04'
    download_file = 'data_in/9080_20210727_E_04.csv'

    # DB Config
    db, live_schema, tmp_schema, user, read_user, host, port = itemgetter(
        'db', 'schema', 'tmp_schema', 'user', 'read_user', 'host', 'port')(conf['pg'])
    print(db, live_schema, tmp_schema, user, read_user, host, port)
    osg_db = OsgPsqlDbLoad(
        db, live_schema, tmp_schema, user, sdtf_type, read_user, host, port)



    # Create 
    osg_db.create_tmp_schema()
    osg_db.psql_create_tables()
    osg_db.psql_authorise_reader_user()
    osg_db.psql_load_data(data_dir)
    # osg_db.psql_add_geom()
    # osg_db.move_temp_to_live()


    # cleanup
    # sdtf_file.cleanup()
    # osgftp.cleanup()

if __name__ == '__main__':
    main()
