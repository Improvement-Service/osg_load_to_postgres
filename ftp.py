import ftp_helpers

class OsgFtp(object):
    def __init__(self, ftp_server, username, password, ftp_ojb=None, file_list=None):
        self.ftp_server = ftp_server
        self.username = username
        self.password = password
        self.ftp_ojb = ftp_ojb
        self.file_list = file_list or []
    
    def connect(self, ftp_server, username, password):
        self.ftp_obj = ftp.connect(ftp_server, username, password)

    def get_ftp_listing(self):
        self.file_list =  ftp_obj.list()

    def get_latest_match(ftp_dir, file_type):
        file
        for file in self.file_list:
            if 
        return file_path
        pass

    def ftp_file_download(ftp_obj, file_path, destination_dir):
        pass
    
    def ftp_file_cleanup():
        """
        Delete files produced by 
        """
        pass