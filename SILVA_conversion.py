# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:41:06 2020

@author: sujin
"""

import pandas as pd 
from tkinter import filedialog

filename = filedialog.askopenfilename()
data = pd.read_excel(filename, index_col = 0, na_values= ['',' - ',0])

reads = data.iloc[:, 7:]
reads_sum = reads.sum(axis = 0).to_frame()
row_count = reads.iloc[:,-1].count()
col_count = reads.count(1)[1]

Number = range(1,7)
Name = ['P_read', 'C_read', 'O_read', 'F_read', 'G_read', 'S_read']
Name_per = ['P(%)', 'C(%)', 'O(%)', 'F(%)', 'G(%)', 'S(%)']
Name_major=['P_rank(%)', 'C_rank(%)', 'O_rank(%)', 'F_rank(%)', 'G_rank(%)', 'S_rank(%)']
Number_name = list(zip(Number, Name, Name_per, Name_major))


def num_to_per(df1, df2, row_count, col_count, r_sum):
    for i in range(0, row_count):
        for j in range(1, col_count+1):
            per = df1.iloc[i,j]/r_sum[0][j-1]*100
            df2.iloc[i,j] = round(per,3)
    return (df2)

def drop_minor(df):
    for idx, row in df.iterrows():
        if row.max() < 1:
            df.drop(idx, inplace = True)
    return (df)
        

for i, j, p, r in Number_name:
    new1 = pd.merge(data.iloc[:, i], reads, left_index = True, right_index = True, how = 'left')
    new2 = new1.copy()
    new2 = num_to_per(new1, new2, row_count, col_count, reads_sum)
    new1 = new1.groupby(new1.iloc[:,0]).sum()
    new2 = new2.groupby(new2.iloc[:,0]).sum()
    new3 = new2.copy()
    new3 = drop_minor(new3)
    with pd.ExcelWriter(filename, mode = 'a', engine = 'openpyxl') as writer:
        new1.to_excel(writer, sheet_name = j)
        new2.to_excel(writer, sheet_name = p)
        new3.to_excel(writer, sheet_name = r)

        

