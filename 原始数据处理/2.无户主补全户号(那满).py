# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

file = r"E:\abc\那满第二次待配.xlsx"

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



    # 把同一户主姓名不存在户主的，以第一行记录，设定为户主   
    for list_tmp in list_1:
        name = df.loc[list_tmp,'姓名']
        name_id = df.loc[list_tmp,'身份证号码']
        break
    
   
    for list_tmp in list_1:
        df.loc[list_tmp,'户主姓名']=name
        df.loc[list_tmp,'户号']=name_id
    



df.to_excel(r"E:\abc\那满第二次待配_已配.xlsx",index=False)

            
        
        