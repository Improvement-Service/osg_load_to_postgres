### Test bed for function written elsewhere

import sdtf_processing
import utils

test = sdtf_processing.SdtfProcessing('DataIn/9010_20210705_E_04.csv', './DataIn', './DataOut')

print(test.filename)

new_dir = test.create_folder()

print(new_dir)

split_files = test.split_sdtf_by_the_record_id(new_dir)