import csv
import PyPDF2
import re
from PyPDF2 import pdf
f = open('e:/python/tutorial/test/TestFiles/Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)

pattern = r'\d{3}.\d{3}.\d{4}'

# print(pdf_reader.numPages)
# text_file = pdf_reader.getPage()
# text = text_file.extractText()
# print(text)
# import os
# os.getcwd()
# print(os.listdir())

# pdf_text = []
# pdf_reader = PyPDF2.PdfFileReader(f)

all_text = ''

for n in range(pdf_reader.numPages):
    
    page = pdf_reader.getPage(n)
    page_text = page.extractText()
    
    all_text = all_text+' '+page_text

match = re.search(pattern,all_text)
print(match.group())


# for n in range(pdf_reader.numPages):
    
#     page  = pdf_reader.getPage(n)
#     page_text = page.extractText()
#     match = re.search(pattern,page_text)
    
#     if match:
#         print(match.group())