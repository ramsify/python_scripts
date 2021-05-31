# =========SQL Output Extractor=========
"""
This script is used to execute SQL and store the output
Provide the Input file path and output file path
Input file contains the actual SQL to be executed
"""
import cx_Oracle
import csv
import pandas as pd

connection = cx_Oracle.connect("HR", "HR", "localhost:1521/orcl",
                               encoding="UTF-8")

with open('D:/Tutorials/Python/files/Query1.sql', 'r') as s:
    sql = s.read()
    s.close()
filename = "D:/Tutorials/Python/files/SQLOutput.csv"
file = open(filename, 'w')
output = csv.writer(file, dialect='excel')

cursor = connection.cursor()
cursor.execute(sql)
query1 = cursor.fetchall()

title = [i[0] for i in cursor.description]
output.writerow(title)

for i in query1:
    output.writerow(i)

cursor.close()
connection.close()
file.close()

with open(filename, 'r') as t:
    content = t.read()
    t.close()
print(content)
