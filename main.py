import argparse
from operator import itemgetter
import utils

def get_input_arg():
    #Variables from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', choices=['a', 'e'], help='sdtf file type: (choose from:  a, e)', required=True)
    args = parser.parse_args()
    return args.type.upper()


def main():
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

    # #########Altnernative using INI.  Config is simpler and more explicit, but more fucntions in utils
    # # Consider using this to make more explicit
    # host, port, db, user, passwd = itemgetter('host','port','db','user')(db_conf)
    # # User config in function then delete afterwards
    # print(host, port, db, user)
    # del host, port, db, user

if __name__ == '__main__':
    main()
