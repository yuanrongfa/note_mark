# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:14:08 2022

@author: HiWin11
"""
import pandas as pd

file = r"C:\Users\HiWin11\Desktop\20220830\百育配对前.xlsx"

df = pd.read_excel(file)


list_add = list(set(df['本户地址']))

for list_add_tmp in list_add:
    
    name = ''        # '姓名'
    name_id = ''     # 户号---name_id----身份证号码
    
    # 每组相同地址，取'户主姓名'=='姓名'
    for person_index in df[df['本户地址']== list_add_tmp].index:
        
        if df.loc[person_index,'户主姓名']==df.loc[person_index,'姓名']:
            
                name = df.loc[person_index,'姓名']
                
                name_id = df.loc[person_index,'身份证号码']
                
    # 根据上面取得的户主对应的身份证作为户号              
    for person_index in df[df['本户地址']==list_add_tmp].index:
        
        df.loc[person_index,'户号']=name_id
    
    
df.to_excel(r"C:\Users\HiWin11\Desktop\20220830\百育已匹配.xlsx",index=False)
        
            
            
        
        