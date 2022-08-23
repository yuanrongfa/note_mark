# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

# 机构号
org_id = '6066'
file = r'/Users/yuan/all.xlsx'

df = pd.read_excel(file,header=0,usecols=['机构','证件号码','贷款金额','贷款余额'],\
                   dtype=str)
    
# 删除制表符
df['机构'] = df['机构'].str.replace(r'\t', '' ,regex=True)
df['证件号码'] = df['证件号码'].str.replace(r'\t', '' ,regex=True)

# df_in表示只有指定机构号的数据
df_in = df[df['机构']=='6066']
#print(df_in.shape)

# 去掉机构用于汇总贷款金额与贷款余额
del df_in['机构']

# 把贷款金额与贷款余额从字符串转成数字型
df_in['贷款金额']=df_in['贷款金额'].astype(float)
df_in['贷款余额']=df_in['贷款余额'].astype(float)

# 以证件号为分组，相当的证件号金额与余额合计
df_in = df_in.groupby('证件号码',as_index=False).sum()
df_in['贷款金额'].sum()
df_in['贷款余额'].sum()
# 计算贷款金额与贷款余额的求和
#df_in['贷款金额'].sum()
#df_in['贷款余额'].sum()
#df_in.shape

df_in.to_excel(r'/Users/yuan/df_in.xlsx')