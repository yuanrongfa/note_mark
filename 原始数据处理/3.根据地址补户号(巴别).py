# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:42:11 2022

@author: fa
"""
import pandas as pd

file = r"E:\abc\巴别.xlsx"

df = pd.read_excel(file)


# 创建去除重复地焉的列表
list_1 = list(set(df['本户地址']))

# 为列表中的每个地址的内容作出循环
for list_tmp in list_1:
    
    # 建立姓名列表，作用是用于取第一个记录作户主，户号
    list_one_name = []
    list_one_id = []
    
    # 为每个地址填充户主、户号
    for i in df[df['本户地址']==list_tmp].index:
        
        # 每次循环都添加到列表，为了取列表的第一个数据
        list_one_name.append(df.loc[i,'姓名'])
        list_one_id.append(df.loc[i,'身份证号码'])
        
        # 把列表的第一个数据，放到相对应的户主姓名、户号
        df.loc[i,'户主姓名']=list_one_name[0]
        df.loc[i,'户号']=list_one_id[0]
        
  
df.to_excel( r"E:\abc\巴别已处理.xlsx",index=False)        
    
