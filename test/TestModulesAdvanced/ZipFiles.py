file1 = open('new_file1.txt','w+')
file1.write('This is file one')
file1.close()

file2 = open('new_file2.txt','w+')
file2.write('This is file two')
file2.close()

import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('new_file1.txt',compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type = zipfile.ZIP_DEFLATED)
comp_file.close()


zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extract_content')

zip_file = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
zip_file.extractall('ext_file')
