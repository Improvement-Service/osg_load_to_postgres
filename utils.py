import configparser
import yaml

def get_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


def get_db_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    db_config = {
        'host': config.get('pg', 'host'),
        'port': config.get('pg', 'port'),
        'user': config.get('pg', 'user'),
        'db': config.get('pg', 'db'),
        'port': config.getint('pg','port')
        }
    return db_config

def get_ftp_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    ftp_config = {
        'host': config.get('ftp','host'),
        'port': config.getint('ftp','port'),
        'user': config.get('ftp', 'user'),
        'passwd': config.get('ftp', 'passwd')
        }
    return ftp_config

def get_dir_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    dir_config = {
        'in': config.get('dirs','in')
        }
    return dir_config