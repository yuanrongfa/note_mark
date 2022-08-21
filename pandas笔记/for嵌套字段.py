import pandas as pd
import openpyxl
import numpy as np


file = r'd:\a1.xlsx'

df=pd.read_excel(file,header=0)

#df.groupby('类别').get_group('硬盘')['收入'].sum()

list_a = list(set(df['姓名']))

for i in list_a:
    list_b=list(set(df[df['姓名']==i]['类别']))
    for j in list_b:
        print(i+j)
    
#df[df['姓名']=='袁荣发']['类别']