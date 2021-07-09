import configparser
import yaml
import os
from pathlib import Path, PurePath

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


class Utils():
    
    def create_child_folder(input_file: str) -> str:
        """Create child otuput folder based on input filename in same parent directory.

        Parameters
        ----
        Args:
            input_file (str): location of file.
        ----
        Returns:
            child_dir (str): full directory of the child directory if created or prexists
        """
        if not Path(input_file).exists():
            raise FileNotFoundError('Input file does not exist')
        if not Path(input_file).is_file():
            print (Path(input_file))
            raise ValueError('Input must be a file. Input must not be a directory')

        f = PurePath(input_file)
        child_dir  = f.parent.joinpath(f.stem)
        if not os.path.exists(child_dir):
            os.mkdir(child_dir)
            print(f'Created child directory:  {child_dir}')
        else:
            print(f'Child directory already existed at:  {child_dir}')
        return str(child_dir)    
    
    def cleanup_safe(directory: str) -> None:
        """Delete all CSV & ZIP files in directory and directory itself. NOT recursive"""
        file_exts = ['csv', 'zip']
        d = Path(directory).absolute()
        files = []
        for ext in file_exts:
            found = d.glob(f'*.{ext}')
            for x in found:
                files.append(x)
        for f in files:
            os.remove(f)
            print(f'Deleted file: {str(f)}')
        os.rmdir(d)
        print(f'Deleted directory: {d}')