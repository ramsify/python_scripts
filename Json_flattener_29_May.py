from copy import deepcopy
import json
import pandas as pd
import os
import glob

dirfile = open('jsondir.txt', "r")
lines = []
for line in dirfile:
    lines.append(line)
dirfile.close()
inpdir = lines[0].rstrip('\n')
opdir =  lines[1].rstrip('\n')
fcnt=0
for file in glob.glob(inpdir+'/sample*.json'):
    fcnt+=1
def cross_join(left, right):
    new_rows = []
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem


def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows


    return pd.DataFrame(flatten_json(data_in))

def jf(e):
    jsonStr = open(inpdir+'/sample' + str(e) + '.json', 'r', encoding='utf8')
    json_data = json.load(jsonStr)
    df = json_to_dataframe(json_data)
    of = opdir+'/Sample_Output' + str(e) + '.xlsx'
    df.to_excel(of, encoding='utf8')
    print('The Json data has been written to: {}'.format(of))
    print("The process has been completed")

if __name__ == '__main__':
    for i in range(1,fcnt+1):
        jf(i)
