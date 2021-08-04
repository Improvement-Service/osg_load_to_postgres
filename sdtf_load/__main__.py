import os
from operator import itemgetter
import sdtf_load.utils as utils
from sdtf_load.osg_ftp import OsgFtp
from sdtf_load.sdtf_processing import SdtfProcessing
from sdtf_load.sdtf_db import OsgPsqlDbLoad

#### CONFIG ####
# SDTF file type to process
sdtf_type = utils.get_input_arg()

# Configuration - see config.yml. Follow structure in config-example.yml
conf = utils.get_config(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'config.yml'
    ), sdtf_type
)

in_dir = conf['directories']['data_in']


# #### FTP DOWNLOAD ####
# # Connect to the FTP site and download the most recent file of right SDTF type.
# FTP config
host, port, user, passwd = itemgetter('host', 'port', 'user', 'passwd')(conf['ftp'])
# FTP object
osgftp = OsgFtp(host, port, user, passwd, sdtf_type)
osgftp.establish_connection()
osgftp.identify_latest_file()
osgftp.download_latest_file(in_dir)

download_file = osgftp.download_file
# download_file = 'data_in/9080_20210727_E_04zip'


### DATA PREP ###
# Create child folder, unzip and split file into component tables
print(f'Processing the following file: {download_file}')
sdtf = SdtfProcessing(download_file)
sdtf.unzip_sdtf()
sdtf.create_folder()
sdtf.split_by_record_id()

data_dir = sdtf.temp_dir
# data_dir = 'data_in/9080_20210727_E_04'


### DB LOAD ###
# DB Config
db, live_schema, tmp_schema, user, read_user, host, port = itemgetter(
    'db', 'schema', 'tmp_schema', 'user', 'read_user', 'host', 'port'
)(conf['pg'])
# DB Processing 
osg_db = OsgPsqlDbLoad(
    db, live_schema, tmp_schema, user, sdtf_type, read_user, host, port
)
# Create schema and add comment of filename
osg_db.create_tmp_schema(sdtf.filename)
osg_db.psql_create_tables()
osg_db.authorise_reader_user()
osg_db.psql_load_data(data_dir)
osg_db.psql_add_geom()
osg_db.move_temp_to_live()


### cleanup ###
sdtf.clean_up()
osgftp.delete_download_file()
