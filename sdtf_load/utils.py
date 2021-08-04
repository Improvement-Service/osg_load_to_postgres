import configparser
import yaml
import os
from pathlib import Path, PurePath
import zipfile
import argparse


def get_input_arg():
    #Variables from command line
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--type', choices=['a', 'e'], help='SDTF file type: (choose from:  a, e)', 
        required=True
        )
    parser.add_argument(
        '-o', '--option', type=int, choices=[1, 2, 3, 4], 
        help='Options.  Choose from...    \
            {1}: download & load latest SDTF,   \
            {2}: download latest SDTF,    \
            {3}: split specific file,    \
            {4}: load specific presplit SDTF', 
        default = 1
        )
    parser.add_argument(
        '-f', '--file', help='SDTF file name.  Only required if using \'option\' 3 (load) or 4 (split) on specific SDTF', 
        required=False
        )
    parser.add_argument(
        '-d', '--directory', help='Directory of SDTF files.  Only required if using \'option\' 3 (load)', 
        required=False
        )
    args = parser.parse_args()
    if args.option == 4 and args.directory is None:
        parser.error("--option requires --directory if set to 4 (load).")
    elif args.option == 3 and args.file is None:
        parser.error("--option requires --file if set to 3 (split SDTF).")
    elif args.option != 3 and args.file:
        parser.error("--file is only required if using \'option\' 3 (split SDTF).")
    elif args.option != 4 and args.directory:
        parser.error("--directory is only required if using \'option\' 4 (load).")


    # return args.type.upper()
    return args #(args.type, args.option, args.file)

def get_config(config_file, sdtf_type):
    """Simple config parsing from yml file"""
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    # Add generic schema into config based on sdtf file type (A or E)
    if sdtf_type.upper() in ['A', 'J']:
        schema = config['pg']['osg_schema']
    elif sdtf_type.upper() in ['E']:
        schema = config['pg']['sg_schema']
    else:
        raise ValueError('SDTF file type unexpected, unable to determine which schema to use')
    config['pg']['schema'] = schema
    return config

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

    
    def unzip_file(zipped_file, extract_folder=None):

        with zipfile.ZipFile(zipped_file, "r") as to_unzip:
            to_unzip.extractall(extract_folder)
            extracted = to_unzip.namelist()
        to_unzip.close()
        return extracted
    
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