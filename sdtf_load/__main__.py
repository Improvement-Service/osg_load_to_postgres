from operator import itemgetter
import sdtf_load.utils as utils
from sdtf_load.osg_ftp import OsgFtp
from sdtf_load.sdtf_processing import SdtfProcessing
from sdtf_load.sdtf_db import OsgPsqlDbLoad

#### CONFIG ####
# SDTF file type to process
# sdtf_type = utils.get_input_arg()
args = utils.get_input_arg()
sdtf_type = args.type
proc_option = args.option
download_file = args.file
data_dir = args.directory

# Configuration - see config.yml. Follow structure in config-example.yml
conf = utils.get_config('./config.yml', sdtf_type)
in_dir = conf['directories']['data_in']

#### FTP DOWNLOAD ####
if proc_option in (1,2):
    # FTP config
    host, port, user, passwd = itemgetter(
        'host', 'port', 'user', 'passwd'
    )(conf['ftp'])

    osgftp = OsgFtp(host, port, user, passwd, sdtf_type)
    osgftp.establish_connection()
    osgftp.identify_latest_file()
    osgftp.download_latest_file(in_dir)
    download_file = osgftp.download_file

### DATA PREP ###
if proc_option in (1,3):
    # Create child folder, unzip and split file into component tables
    sdtf = SdtfProcessing(download_file)
    sdtf.unzip_sdtf()
    sdtf.create_folder()
    sdtf.split_by_record_id()
    data_dir = sdtf.temp_dir

###  DB load ###
if proc_option in (1,4):
    # DB Config
    db, live_schema, tmp_schema, user, read_user, host, port = itemgetter(
        'db', 'schema', 'tmp_schema', 'user', 'read_user', 'host', 'port'
    )(conf['pg'])

    osg_db = OsgPsqlDbLoad(
        db, live_schema, tmp_schema, user, sdtf_type, read_user, host, port
    )
    # Create schema and add comment of filename
    osg_db.create_tmp_schema(data_dir)
    osg_db.psql_create_tables()
    osg_db.authorise_reader_user()
    osg_db.psql_load_data(data_dir)
    osg_db.psql_add_geom()
    osg_db.move_temp_to_live()

### cleanup ###
if proc_option in (1,):

    sdtf.clean_up()
    osgftp.delete_download_file()
