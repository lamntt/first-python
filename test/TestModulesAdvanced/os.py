f = open('practices.txt','w+')
f.write('This is a text file.')
f.close()

import os
os.getcwd()
print(os.listdir())

file_path = 'e:/python/tutorial/test'
for folder , sub_folders , files in os.walk(file_path):
    
    print("Currently looking at folder: "+ folder)
    # print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    # print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
