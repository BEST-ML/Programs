# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:33:23 2020

@author: sujin
"""
import pandas as pd 
from tkinter import filedialog
#import data
filename = filedialog.askopenfilename()
data1 = pd.read_excel(filename, sheet_name = 0, na_values= ['nan', ' ',''], usecols = "A:B", header = None, index_col = 0)
data2 = pd.read_excel(filename, sheet_name = 1, index_col = 0, na_values= ['nan', ' ', ''])

#search name frome the namemap.txt
filename = filedialog.askopenfilename()
namemap = pd.read_table(filename,index_col = 0, sep = '\\', header = None)
namemap = namemap.T
data2 = pd.concat([namemap, data2], join = 'inner')
data2.rename(columns = data2.iloc[0], inplace = True)
data2.drop(index = 1, inplace = True)

data1.index = data1.index.astype('str')
name_split = data1.index.str.split(";")
data1.index = name_split.str.get(0)                                   
data1.iloc[:,0] = data1.iloc[:,0].astype('str')
split = data1.iloc[:,0].str.split(";")

num = range(0,7)
col_names = ['Domain', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
num_col = list(zip(num, col_names))
for i, n in num_col:
    data1[n] = split.str.get(i)
data1.drop(data1.columns[[0]], axis = 'columns', inplace = True)

for i, n in num_col:
    split = data1.iloc[:,i].str.split("__")
    data1[n] = split.str.get(-1)

data = pd.merge(data1, data2, left_index = True, right_index = True, how = 'left')
data = data[data['Domain'] != 'Unclassified']
reads = data.iloc[:, 7:]
reads_sum = reads.sum(axis = 0).to_frame()
col_count = reads.count(1)[1]
row_count = reads.iloc[:,-1].count()

unid = ['uncultured', 'unidentified', 'Ambiguous', 'metagenome', 'Unknown']
for j in range(0, 7):
    for i in range(0, row_count):
        if any(f in str(data.iloc[i,j]) for f in unid):
            data.iloc[i,j] = 'unidentified'
            
data = data.fillna('unidentified')
 
def domain(df):
    check = df.groupby(df.iloc[:,0]).sum()
    return (check)
    
def num_to_per(df, col_count, r_sum):
    for i in range(0, len(df)):
        for j in range(0, col_count):
            per = df.iloc[i,j]/r_sum.iloc[j][0] * 100
            df.iloc[i,j] = round(per,3)
    return (df)

check_domain = domain(data)
check_domain = num_to_per(check_domain, col_count, reads_sum)
excel = 'domain.xlsx'
check_domain.to_excel(excel_writer=excel, sheet_name = "domain")
print(check_domain)

ask_drop = input("drop the minor domain? [y/n] : ")

if ask_drop == 'y':
    drop_domain = input("which domain should we drop ? answer [A/B] : ")
    if drop_domain == 'A':
        drop_domain = 'Archaea'
    elif drop_domain == 'B':
        drop_domain = 'Bacteria'
    new = data[data.iloc[:,0] != drop_domain]
    file = input("file name (add .xlsx) : ")
    new.to_excel(excel_writer=file, sheet_name = "OTUs")
else:
    file = input("file name (add .xlsx): ")
    data.to_excel(excel_writer=file, sheet_name = "OTUs")

'''
import subprocess
subprocess.call(['python3', 'SILVA_conversion.py', file])
'''





































   
