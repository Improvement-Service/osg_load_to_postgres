from ftplib import FTP_TLS
import socket

#import sys
from datetime import datetime
#import csv
import re
import os

class ExplicitTLS(object):
    """
    This class is used to establish secure Explicit FTP secure connections.
    """

    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        #A FTP subclass which adds TLS support to FTP.
        self.client = FTP_TLS(timeout=10)

    def setup(self):
        #A FTP subclass which adds TLS support to FTP.
        self.client = FTP_TLS(timeout=10)
        #Set the instance’s debugging level. This controls the amount of debugging output printed.
        #self.client.set_debuglevel(1)

    def connect(self):
        # Connect to the given host and port.
        self.client.connect(host=self.host, port=self.port)

    def login(self):
        # Log in as the given user.
        self.client.login(user=self.user, passwd=self.passwd)
        #Make our connection to the server secure (i.e. encrypted)
        self.client.prot_p()
        #This is a hack making 'ftplib' use the EPSV network protocol (i.e. an IPv6 connection) instead of the PASV
        #protocol (i.e. an IPv4). The reason for doing this is that there is a bug in FTP lib which returns the wrong
        #IP address after connection to the FTP if PASV is used. In contrast if the EPSV protocol is used the FTP IP is
        #returned correctly allowing further commands to the FTP connection.
        self.client.af = socket.AF_INET6
        return self.client

    def tear_down(self) -> None:
        """Close the FTP connection unilaterally.  :return: None"""
        self.client.close()


class OsgFtp(ExplicitTLS):

    def __init__(self, host, port, user, passwd, sdtf_type, sdtf_version=4):
        super().__init__(host, port, user, passwd)
        self.sdtf_type = sdtf_type
        self.sdtf_version = sdtf_version
        self.latest_file = None
        self.download_file = None

    #self = ExplicitTLS(host, port, user, passwd)

    # def __init__(self, host, port, user, passwd):
    #     super(ExplicitTLS, self).__init__(host, port, user, passwd)
    #     ftpes = ExplicitTLS(self.host, self.port, self.user, self.passwd)

    def establish_connection(self):
        self.setup()
        self.connect()
        self.login()

    def print_all_ftp_files(self):
        for file_name in self.client.nlst():
            print(file_name)

    def identify_latest_file(self):
        """(ftplib object) -> str
        Args:
            cleint (object):  object returned from ftplib
            sdtf_version (int):  Integer (either 2 or 4) determining the sdtf version file to download.
            sdtf_type (str):  String (either A or E) determining the sdtf type file to download.

        Returns the 'SDTF' file which will be downloaded in the local machine for further processing.
        client should be an obejct returned by
        >>>identify_most_recent_file_available_in_the_ftp_server(obj)
        '9080_20180102_A_01_242.zip'
        >>>identify_most_recent_file_available_in_the_ftp_server(obj)
        None
        """
        ## PROBLEM - multiple OSG export jobs can produce files of same name.  any bespoke export such as including mutliple LAs
        ## results in organisation code of Improvement Service (9080).   Therefore the only way to guaruntee the right file is processed
        ## is to set this script to run shortly after OSG export job has completed.

        # Determine which filename pattern to use based on sdtf verion (2 or 4) and type (A or E)
        if str(self.sdtf_version) == '2' and self.sdtf_type.upper() == 'A':
            re_test = re.compile('9080_\d{8}_A_01.zip')
        elif str(self.sdtf_version) == '4' and self.sdtf_type.upper() == 'A':
            re_test = re.compile('9080_\d{8}_A_04.zip')
        elif str(self.sdtf_version) == '2' and self.sdtf_type.upper() == 'E':
            re_test = re.compile('9080_\d{8}_E_01.zip')
        elif str(self.sdtf_version) == '4' and self.sdtf_type.upper() == 'E':
            re_test = re.compile('9080_\d{8}_E_04.zip')
        else:
            re_test = None
        # Build list of tuples (date, filename)
        files_dates = [(datetime.strptime(file_name.split('_')[1], '%Y%m%d').date(), file_name)\
                       for file_name in self.client.nlst() if re_test.match(file_name)]
        #Identify the file which is the most recent using the files_dates list and return it as an output from this
        #function.
        if len(files_dates) > 0:
            # Sort by proper date in lists, then pull out proper name
            self.latest_file = sorted(files_dates, key=lambda x: x[0], reverse=True)[0][1]
            print("Latest file found:  " + str(self.latest_file))
        else:
            self.latest_file = None
            print("No file matching type: {} and version: {}".format(self.sdtf_type, self.sdtf_version))
        return self.latest_file

    def download_latest_file(self,download_folder):

        #An FTP RETR command needs to be used to download the identified file.
        retr_command = f'RETR {self.latest_file}'
        if not os.path.exists(download_folder):
            os.mkdir(download_folder)

        #This is where the file will be held.
        self.download_file = download_folder + '/' + self.latest_file

        with open(self.download_file, 'wb') as f:
            self.client.retrbinary(retr_command, f.write)

        return self.download_file

    def delete_download_file(self):
        try:
            os.remove(self.download_file)
            print(f'Deleted file: {self.download_file}')
        except:
            pass
