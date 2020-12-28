import pandas as pd
import numpy  as np
import xlrd
import os

#df = pd.read_csv("try.csv")
#print(df)

#df1=pd.read_excel("Excel_test.xlsx",engine='openpyxl',)
#print(df1)


# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('Test.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
#print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

if "Quickborn" in pageObj.extractText():
    print(f"Quickborn in pageObj.extractText()")

# closing the pdf file object
pdfFileObj.close()
