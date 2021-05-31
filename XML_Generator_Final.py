# ==========XML file generator for Input and Output XML==========#
'''
This file takes 3 inputs
baseinput.xml
xmlinput csv (field values for xml)
Endpoint URL for request & response
'''

# Regexp for XML tag - (>.[^(><.)]+<)
import pandas as pd
import csv
import requests
import os
from bs4 import BeautifulSoup

global cnt
df = pd.read_csv('xi.csv', keep_default_na=False)


# print(len(df))
# print(type(r))

def convert_row(row):
    global r
    r = []
    for j in range(0, 4):
        r.append(row[j])
    # global cnt
    print(r)
    fname = 'baseinput.xml'
    with open(fname, 'r') as x:
        xml = x.read()
        x.close()
    # print(xml)
    xml_edit = xml % tuple(r)
    # print(xml_edit)
    with open('Input' + str(i) + '.xml', 'w') as f:
        f.write(xml_edit)
        f.close()


i = 1
for index, row in df.iterrows():
    if i > len(df):
        break
    else:
        convert_row(row)
        i += 1
# print (cnt)
dir = str(os.getcwd())
dir = dir.replace('\\', '/')
print("Input XMLS have been successfully generated. \n")
print("The directory of XML files: ", dir)
url = "http://dnvqaapmdm05.corpzone.internalzone.com:8280/MDMWebService/searchUpsertDelPartySOAP"


def searchreq(x):
    st = ''
    f = open(x, 'r')
    inp = f.read()
    f.close()
    response = requests.post(url, data=inp)
    op = response.text
    with open('Output' + str(i) + '.xml', 'w') as t:
        t.write(op)
        t.close()
    with open('Output' + str(i) + '.xml', 'r') as u:
        for line in u:
            st += line
        df = (BeautifulSoup(st, 'lxml').prettify())
        u.close()
    # print("DF: \n",df)
    with open('Output' + str(i) + '.xml', 'w') as v:
        v.write(df)
        v.close()


for i in range(1, len(df) + 1):
    searchreq('Input' + str(i) + '.xml')
print("Output files have been generated successfully")
