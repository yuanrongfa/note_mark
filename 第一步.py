# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

# 账户机构号
org_id = '6066'
#file = r'/Users/yuan/all.xlsx'
file = r'd:\all.xlsx'

print('正在读取总表请稍后...')
df = pd.read_excel(file,header=0,usecols=['账户机构','证件号码','贷款金额','贷款余额'],\
                   dtype=str)
    
# 删除制表符
df['账户机构'] = df['账户机构'].str.replace(r'\t', '' ,regex=True)
df['证件号码'] = df['证件号码'].str.replace(r'\t', '' ,regex=True)
print('正在导出all_df表，请稍后...')
df.to_excel(r'd:\df_all.xlsx')

# -----------------------------------df_in的开始----------------------------
# df_in表示只有指定账户机构号的数据
df_in = df[df['账户机构']=='6066']
#print(df_in.shape)

# 去掉账户机构用于汇总贷款金额与贷款余额
del df_in['账户机构']

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

print('正在导出df_in表，请稍后...')
#df_in.to_excel(r'/Users/yuan/df_in.xlsx')
df_in.to_excel(r'd:\df_in.xlsx')
# ------------------------------------df_in的结束---------------------------

# ------------------------------------df_out的开始--------------------------
# df_out表示只有非指定账户机构号的数据,取反用'~'
df_out = df[~(df['账户机构']=='6066')]
#print(df_out.shape)

# 去掉账户机构用于汇总贷款金额与贷款余额
del df_out['账户机构']

# 把贷款金额与贷款余额从字符串转成数字型
df_out['贷款金额']=df_out['贷款金额'].astype(float)
df_out['贷款余额']=df_out['贷款余额'].astype(float)

# 以证件号为分组，相当的证件号金额与余额合计
df_out = df_out.groupby('证件号码',as_index=False).sum()
df_out['贷款金额'].sum()
df_out['贷款余额'].sum()
# 计算贷款金额与贷款余额的求和
#df_out['贷款金额'].sum()
#df_out['贷款余额'].sum()
#df_out.shape

print('正在导出df_out表，请稍后...')
#df_out.to_excel(r'/Users/yuan/df_out.xlsx')
df_out.to_excel(r'd:\df_out.xlsx')
# ------------------------------------df_out的结束---------------------------



