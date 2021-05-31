# ============CSV validation========
"""
This Script compares 2 csv files and highlight the differences.
"""
import os
import csv
import pandas as pd

# define parameters
# path to files

src_filename = "D:\\Tutorials\\Python\\files\\src.csv"
tgt_filename = "D:\\Tutorials\\Python\\files\\tgt.csv"

os.getcwd()
# list of key column(s)
key = ['LOCATION_ID']
# sheets to read in
sheet = 'Sheet1'

# Read in the two excel files and fill NA
old = pd.read_csv(src_filename, keep_default_na=False)
new = pd.read_csv(tgt_filename, keep_default_na=False)
# set index
old = old.set_index(key)
new = new.set_index(key)

# adding Multilevel columns
old.columns = pd.MultiIndex.from_product([['old'], old.columns])
new.columns = pd.MultiIndex.from_product([['new'], new.columns])

# identify dropped rows and added (new) rows
dropped_rows = set(old.index) - set(new.index)
added_rows = set(new.index) - set(old.index)

# combine data
# df_all_changes1 = pd.concat([old, new], axis='columns', keys=['old','new'], join='outer')

df_all_changes = old.merge(new, how="outer", on="LOCATION_ID")

# swap column indexes
df_all_changes = df_all_changes.swaplevel(axis='columns')  # [new.columns[0:]]


# prepare function for comparing old values and new values
def report_diff(x):
    return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)


# apply the report_diff function
df_changed = df_all_changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis=1))

# create 3 datasets:
# diff - contains the differences
# dropped - contains the dropped rows
# added - contains the added rows
diff = df_changed[df_changed.apply(lambda x: x.str.contains("--->") == True, axis=1)]
dropped = old.loc[dropped_rows]
added = new.loc[added_rows]

# create a name for the output excel file
fname = 'D:/Tutorials/Python/files/Report.xlsx'

# write dataframe to excel
writer = pd.ExcelWriter(fname, engine='xlsxwriter')
df_all_changes.to_excel(writer, sheet_name='Merged', index=True)
df_changed.to_excel(writer, sheet_name='Merge Group', index=True)
diff.to_excel(writer, sheet_name='Diff', index=True)
dropped.to_excel(writer, sheet_name='Missing in Tgt', index=True)
added.to_excel(writer, sheet_name='Inserted only in Tgt', index=True)

# get xlswriter objects
workbook = writer.book
worksheet = writer.sheets['Diff']
worksheet.hide_gridlines(2)
worksheet.set_default_row(15)

# get number of rows of the df diff
row_count_str = str(len(diff.index) + 1)

# define and apply formats
highligt_fmt = workbook.add_format({'font_color': '#FF0000'})
worksheet.conditional_format('A1:ZZ' + row_count_str, {'type': 'text', 'criteria': 'containing', 'value': '--->',
                                                       'format': highligt_fmt})
# save the output
writer.save()
print('\nDone.\n')
