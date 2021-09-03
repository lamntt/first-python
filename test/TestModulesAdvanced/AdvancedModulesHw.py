import shutil
import os
import re

os.getcwd()
shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

pattern = r'\d{3}-\d{3}-\d{4}'
def search(file,pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

result = []

file_path = 'e:/python/tutorial/extracted_content'
for folder , sub_folders , files in os.walk(file_path):
    for f in files:
        # print(files)
        full_path = folder + '\\' + f
        result.append(search(full_path))


for r in result:
    if r != '':
        print(r.group())