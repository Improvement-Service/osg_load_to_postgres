import sdtf_load.utils as utils
import csv
import os
import itertools
import re

class SdtfProcessing(object):
    """
    Processing class for SDTF files.  This includes methods for unzipping, splitting into tables for processing.
    """
    osg_table_ids = [
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    29,
                    30,
                    31,
                    32,
                    51,
                    52,
                    53,
                    93,
                    99
                    ]
    
    def __init__(self, filename):
        self.filename = filename
        self.temp_dir = None
        self.temp_files = None
        self.extracted_file = None

    def sdtf_unzip():
        pass
    
    def create_folder(self):
        """Create otuput folder based on input filename
        Args:
            input_file (str): name of file.   
        """
        out_dir = utils.Utils.create_child_folder(self.filename) 
        self.temp_dir = out_dir
        print(f'Temporary working directory: {self.temp_dir}')
        return out_dir
    
    def unzip_sdtf(self) -> list:
        """ 
        Extract SDTF from archive into same folder.  Set extracted_file attribute on object.  
        Return extracted file(s) in list.  Raise error if more than one file.
        """
        unzipped = utils.Utils.unzip_file(self.filename, os.path.dirname(self.filename))
        if len(unzipped) > 1:
            raise ValueError('Zip archive "{}" expected to return 1 file, however returned {}.  These were: {}'
            .format(self.filename, len(unzipped), unzipped))
        self.extracted_file = os.path.join(os.path.dirname(self.filename), unzipped[0])
        print(f'Extracted file:  {self.extracted_file}')
        return unzipped


    # def split_sdtf_by_the_record_id(self):
    #     """
    #     Takes input file and splits input csv into multiple files based on first column. Input file is derived from 
    #     self.extracted_file

    #     Parameters
    #     -------
    #     Args:
    #         self

    #     Returns:
    #         tables_output (list): List of output files. These should be integers representing table identifiers.
    #     """
    #     if self.extracted_file is None:
    #         raise AttributeError('Attribute extracted_file is not set.  Ensure the file is correctly unzipped first')
    #     # Reader - note use of no quotations; aim is to maintain data as unchanged.
    #     reader = csv.reader(open(self.extracted_file, 'r', encoding='utf-8-sig', newline='\n'), 
    #                         delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE, skipinitialspace=True)
    #     tables_output = []

    #     # The groupby function is used to create chunks of data rows using the record_identifier as the group column.
    #     for record_identifier, rows in itertools.groupby(reader, lambda row: row[0]):
    #         # Catch any invalid 
    #         try:
    #             output_file = self.temp_dir + '/{}.csv'.format(record_identifier)
    #             tables_output.append(output_file)
    #             with open(output_file, 'w', newline='\n', encoding='utf8') as output_file:
    #                 # Check to make sure record identifier in osg_tables
    #                     if not int(record_identifier) in self.osg_table_ids:
    #                         raise ValueError(print('SDTF record identifier {} not in expected list'.format(record_identifier)))
    #                     # Writer - note use of no quotations, these are preserved from reading.
    #                     else:
    #                         csv_writer = csv.writer(output_file, delimiter=',', quotechar='', quoting=csv.QUOTE_NONE, escapechar='')
    #                         for row in rows:
    #                             csv_writer.writerow(row)
    #         except:
    #             print('There is an issue with record_identifier. Possibly rogue line break.  Check following row:')
    #             for row in rows:
    #                 try:
    #                     int(row[0])
    #                 except:
    #                     print(row)
    #     print('Output {num} files with table ids:{ids}'.format(num=len(tables_output), ids=tables_output))
    #     file_list = [str(x)+'.csv' for x in tables_output]
    #     self.temp_files = tables_output
    #     return tables_output     
    
    def split_by_record_id(self):
        """
        Takes input file and splits input csv into multiple files based on first column. Input file is derived from 
        self.extracted_file

        Parameters
        -------
        Args:
            self

        Returns:
            Sets self.file_list.
        """
            # Regex for table_id.  Ignore others which don't match
        record_id_pattern = re.compile(r'\d\d\,')
        outputs = {}
        file_list = []

        with open(self.extracted_file, 'r', encoding='utf-8-sig', newline='') as file:
            for line in file:
                # Make sure table_id follows pattern
                if re.match(record_id_pattern, line):
                    record_id = line.split(',')[0]
                    if not int(record_id) in self.osg_table_ids:
                        raise ValueError('SDTF record identifier {} not in expected list'.format(record_id))
                
                # Now write, add to existing writer or create new
                if record_id in outputs.keys(): 
                    outputs[record_id].write(line)
                else:
                    output_file = os.path.join(self.temp_dir, '{}.csv'.format(record_id))
                    outputs[record_id] = open(output_file, 'w', newline='\n', encoding='utf8')
                    outputs[record_id].write(line)
                    file_list.append(output_file)
            # Close writers
            for v in outputs.values():
                v.close()
            
        print('Output {num} with table ids :{file_ids}'.format(num=len(outputs.values()), file_ids=file_list))   
        self.temp_files = file_list

    def clean_up(self):
        """Remove all split files and original"""
        # Safely remove temp directory and temp files within 
        utils.Utils.cleanup_safe(self.temp_dir)
        try:
            os.remove(self.extracted_file)
            print(f'Deleted file: {self.extracted_file}')
        except:
            pass