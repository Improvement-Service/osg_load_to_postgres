import utils
import csv
import itertools

class SdtfProcessing(object):
    """
    Processing class for SDTF files.  This includes methods for unzipping, splitting into tables for processing, 
    checking table ids for acceptable range.
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
    
    def __init__(self, filename, temp_in, temp_out):
        self.filename = filename
        self.temp_in = temp_in
        self.temp_out = temp_out

    def sdtf_unzip():
        pass
    
    def create_folder(self):
        """Create otuput folder based on input filename
        Args:
            input_file (str): name of file.   
        """
        out_dir = utils.Utils.create_child_folder(self.filename) 
        return out_dir
    
    
    def split_sdtf_by_the_record_id(self, out_folder):
        """Takes input file and folder, splits input csv into multiple files based on first column

        Parameters
        -------
        Args:
            file (str): 
                Absolute path of file to be split
            out_folder(str): 

        Returns:
            tables_output (list): List of output files. These should be integers representing table identifiers.
        """
        # Reader - note use of no quotations; aim is to maintain data as unchanged.
        reader = csv.reader(open(self.filename, 'r', encoding='utf-8-sig', newline='\n'), 
                            delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)

        tables_output = []

        # The groupby function is used to create chunks of data rows using the record_identifier as the group column.
        for record_identifier, rows in itertools.groupby(reader, lambda row: row[0]):
            tables_output.append(int(record_identifier))
            
            with open(out_folder + '\\{}.csv'.format(record_identifier), 'w', newline='\n', encoding='utf8') as output_file:

                # Check to make sure record identifier in osg_tables
                if not int(record_identifier) in self.osg_table_ids:
                    raise ValueError(print('SDTF record identifier {} not in expected list'.format(record_identifier)))

                # Writer - note use of no quotations, these are preserved from reading.
                else:
                    csv_writer = csv.writer(output_file, delimiter=',', quotechar='', quoting=csv.QUOTE_NONE, escapechar='')
                    for row in rows:
                        csv_writer.writerow(row)
                

        print('Output {num} files with table ids:{ids}'.format(num=len(tables_output), ids=tables_output))
        return tables_output     
    
    def clean_up():
        """Remove all split files and original"""