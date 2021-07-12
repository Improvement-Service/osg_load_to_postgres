from ftplib import FTP_TLS

import sys
from datetime import datetime
import ftp_helpers as fth
import configuration
import csv
import re

class ExplicitTLS(object):
    """
    This class is used to establish secure Explicit FTP secure connections.
    """

    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

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





class DownloadNationalExtract(ExplicitTLS):

    #self = ExplicitTLS(host, port, user, passwd)

    # def __init__(self, host, port, user, passwd):
    #     super(ExplicitTLS, self).__init__(host, port, user, passwd)
    #     ftpes = ExplicitTLS(self.host, self.port, self.user, self.passwd)

    def establish_secure_authenticated_connection_to_ftp(self):
        self.setup()
        self.connect()
        return self.login()

    def all_ftp_files(self, client):
        for file_name in client.nlst():
            print(file_name)

    def identify_most_recent_file_available_in_the_ftp_server(self,client, sdtf_version, sdtf_type):
        """(ftplib object) -> str
        Args:
            cleint (object):  object returned from ftplib
            sdtf_version (int):  Integer (either 2 or 4) determining the sdtf version file to download.
            sdtf_type (str):  String (either A or E) determining the sdtf type file to download.

        Returns the 'SDTF' file which will be downloaded in the local machine for further processing.
        client should be an obejct returne dby
        >>>identify_most_recent_file_available_in_the_ftp_server(obj)
        '9080_20180102_A_01_242.zip'
        >>>identify_most_recent_file_available_in_the_ftp_server(obj)
        None
        """

        #NOTE THE FOLLOWING HAS BEEN COMMENTED OUT DUE TO OSG FTP FOLDER STRUCTURE CHANGE.  CHANGE DIRECTEY NO LONGER NECESSARY
        #Change working directory to 'DOWNLOAD'. 
        #client.cwd('DOWNLOAD')

        #In a list of lists hold the extract datetime and the file name for each file in the FTP server within the DOWNLOAD
        #folder. Each nested list within the list represents the data for each file. An example of the output for the
        #file_dates list is: [[datetime.date(2018, 1, 2), '9080_20180102_A_01_242.zip'], [datetime.date(2018, 1, 9), \
        # '9080_20180109_A_01_242.zip'], [datetime.date(2018, 1, 16), '9080_20180116_A_01_242.zip'], \
        #[datetime.date(2018, 1, 23),'9080_20180123_A_01_242.zip'],[datetime.date(2018, 1, 30),'9080_20180130_A_01_242.zip'],\
        #[datetime.date(2018, 2, 6),'9080_20180206_A_01_242.zip'],[datetime.date(2018, 2, 13),'9080_20180213_A_01_242.zip']]
        
        ## NOTE ## Filenameing structure was changed to remove the ID of the OSG export job (i.e. 242).
        ## now you must rely on the filename alone (e.g. 9080_20180206_A_01.zip)
        ## PROBLEM - multiple OSG export jobs can produce files of same name.  any bespoke export such as including mutliple LAs
        ## results in organisation code of Improvement Service (9080).   Therefore the only way to guaruntee the right file is processed
        ## is to set this script to run shortly after OSG export job has completed.


        # Determine which filename pattern to use based on sdtf verion (2 or 4) and type (A or E)

        if str(sdtf_version) == '2' and sdtf_type.upper() == 'A':
            re_test = re.compile('9080_\d{8}_A_01.zip')
        elif str(sdtf_version) == '4' and sdtf_type.upper() == 'A':
            re_test = re.compile('9080_\d{8}_A_04.zip')
        elif str(sdtf_version) == '2' and sdtf_type.upper() == 'E':
            re_test = re.compile('9080_\d{8}_E_01.zip')
        elif str(sdtf_version) == '4' and sdtf_type.upper() == 'E':
            re_test = re.compile('9080_\d{8}_E_04.zip')
        else:
            re_test = None

        # Build list of lists [file_date & filename]
        files_dates = [[datetime.strptime(file_name.split('_')[1], '%Y%m%d').date(), file_name]\
                       for file_name in client.nlst() if re_test.match(file_name)]

        #Identify the file which is the most recent using the files_dates list and return it as an output from this
        #function.
        if len(files_dates) > 0:
            # Sort by proper date in lists, then pull out proper name
            most_recent_ftp_date = sorted(files_dates, key=lambda x: x[0], reverse=True)[0][1]
            print("Latest file found:  " + str(most_recent_ftp_date))
        else:
            most_recent_ftp_date = None
            print("No file matching type: {} and version: {}".format(sdtf_type, sdtf_version))

        return most_recent_ftp_date

    def download_the_most_recent_file_using_the_ftp(self, client,file_name,download_folder):

        #An FTP RETR command needs to be used to download the identified file.
        retr_command = f'RETR {file_name}'

        #This is where the file will be held.
        download_file = download_folder + '\\' + file_name

        with open(download_file, 'wb') as f:
            client.retrbinary(retr_command, f.write)

        return file_name

def main(download_folder, sdtf_version, file_type):

    df = DownloadNationalExtract(insert_config_here)
    client = df.establish_secure_authenticated_connection_to_ftp()
    #df.all_ftp_files(client)
    file_name = df.identify_most_recent_file_available_in_the_ftp_server(client, sdtf_version, file_type)
    if file_name is not None:
        filename = df.download_the_most_recent_file_using_the_ftp(client, file_name,download_folder)
    else:
        filename = None

    return filename

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])