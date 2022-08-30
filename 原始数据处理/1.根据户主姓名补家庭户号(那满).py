# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

file = r"E:\abc\那满.xlsx"

df = pd.read_excel(file)

list_1 = []


i = 0





while i<len(df):
    name = ''
    name_id = ''
    
    list_1 = []
    b =True
    list_1.append(i)
    while b:
        if df.loc[i,'户主姓名']==df.loc[i+1,'户主姓名']:
            list_1.append(i+1)
            i= i +1
        else:
            i = i+1
            
            b=False
        
    for list_tmp in list_1:
        if df.loc[list_tmp,'户主姓名']==df.loc[list_tmp,'姓名']:
            name=df.loc[list_tmp,'姓名']
            name_id=df.loc[list_tmp,'身份证号码']
    
    for list_tmp in list_1:
        df.loc[list_tmp,'户号']=name_id
    
    print('----------------------------')


df.to_excel(r"E:\abc\那满已匹配.xlsx",index=False)

            
        
        