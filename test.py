### Test bed for function written elsewhere
import argparse
from operator import itemgetter
import utils
import sdtf_processing

# test = sdtf_processing.SdtfProcessing('DataIn/9010_20210705_E_04.csv', './DataIn', './DataOut')

# print(test.filename)

# new_dir = test.create_folder()

# print(new_dir)

# split_files = test.split_sdtf_by_the_record_id(new_dir)



def

def main(download_folder, sdtf_version, file_type):
    # SDTF file type to process
    sdtf_type = get_input_arg()
    print(sdtf_type)

    # Configuration - see config.yml. Follow structure in config-example.yml
    conf = utils.get_config('./config.yml')
    # db_conf = utils.get_db_config('./config.ini')
    # ftp_conf = utils.get_ftp_config('./config.ini')
    # dir_conf = utils.get_dir_config('./config.ini')
    
    # Consider using this to make more explicit
    host, port, db, user = itemgetter('host','port','db','user')(conf['pg'])
    # User config in function then delete afterwards
    print(host, port, db, user)
    del host, port, db, user


    # df = DownloadNationalExtract(insert_config_here)
    # client = df.establish_secure_authenticated_connection_to_ftp()
    # #df.all_ftp_files(client)
    # file_name = df.identify_most_recent_file_available_in_the_ftp_server(client, sdtf_version, file_type)
    # if file_name is not None:
    #     filename = df.download_the_most_recent_file_using_the_ftp(client, file_name,download_folder)
    # else:
    #     filename = None

    # return filename

if __name__ == "__main__":
    main()
    # main(sys.argv[1], sys.argv[2], sys.argv[3])