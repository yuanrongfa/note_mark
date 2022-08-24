# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import datetime



# 账户机构号
org_id = '6093'
#file = r'/Users/yuan/all.xlsx'
file = r'd:\all.xlsx'
file_huji = r'd:\玉凤坤平户籍.xlsx'

print('正在读取总表请稍后...')
df = pd.read_excel(file,header=0,usecols=['账户机构','证件号码','贷款金额','贷款余额'],\
                   dtype=str)
    
# 删除制表符
df['账户机构'] = df['账户机构'].str.replace(r'\t', '' ,regex=True)
df['证件号码'] = df['证件号码'].str.replace(r'\t', '' ,regex=True)
#print('正在导出all_df表，请稍后...')
#df.to_excel(r'd:\df_all.xlsx')

# 以证件号为分组，相当的证件号金额与余额合计,总表groupby后的贷款金额和余额
df_all=df
# 把贷款金额与贷款余额从字符串转成数字型
df_all['贷款金额']=df_all['贷款金额'].astype(float)
df_all['贷款余额']=df_all['贷款余额'].astype(float)
df_all = df_all.groupby('证件号码',as_index=False).sum()
# 计算贷款金额与贷款余额的求和
#df_all['贷款金额'].sum()
#df_all['贷款余额'].sum()
#df_all.shape

# -----------------------------------df_in的开始----------------------------
# df_in表示只有指定账户机构号的数据
df_in = df[df['账户机构']==org_id]
#print(df_in.shape)

# 去掉账户机构用于汇总贷款金额与贷款余额
del df_in['账户机构']

# 把贷款金额与贷款余额从字符串转成数字型
df_in['贷款金额']=df_in['贷款金额'].astype(float)
df_in['贷款余额']=df_in['贷款余额'].astype(float)

# 以证件号为分组，相当的证件号金额与余额合计
df_in = df_in.groupby('证件号码',as_index=False).sum()
# 计算贷款金额与贷款余额的求和
#df_in['贷款金额'].sum()
#df_in['贷款余额'].sum()
#df_in.shape

#print('正在导出df_in表，请稍后...')
#df_in.to_excel(r'/Users/yuan/df_in.xlsx')
#df_in.to_excel(r'd:\df_in.xlsx')
# ------------------------------------df_in的结束---------------------------

# ------------------------------------df_out的开始--------------------------
# df_out表示只有非指定账户机构号的数据,取反用'~'
df_out = df[~(df['账户机构']==org_id)]
#print(df_out.shape)

# 去掉账户机构用于汇总贷款金额与贷款余额
del df_out['账户机构']

# 把贷款金额与贷款余额从字符串转成数字型
df_out['贷款金额']=df_out['贷款金额'].astype(float)
df_out['贷款余额']=df_out['贷款余额'].astype(float)

# 以证件号为分组，相当的证件号金额与余额合计
df_out = df_out.groupby('证件号码',as_index=False).sum()
# 计算贷款金额与贷款余额的求和
#df_out['贷款金额'].sum()
#df_out['贷款余额'].sum()
#df_out.shape

#print('正在导出df_out表，请稍后...')
#df_out.to_excel(r'/Users/yuan/df_out.xlsx')
#df_out.to_excel(r'd:\df_out.xlsx')
# ------------------------------------df_out的结束---------------------------


# ------------------------------------匹配的开始-----------------------------
print('正在读取玉凤坤平户籍文件，请稍后...')
df_huji = pd.read_excel(file_huji,header=0,dtype=str)
df_huji = df_huji[df_huji['机构']==org_id]

# 匹配df_in，匹配本机构的数据
df_results = pd.merge(df_huji, df_in, left_on='身份证号码', right_on='证件号码', \
                      how='left')
del df_results['证件号码']
# 修改增加项为本机构贷款金额、余额
df_results.rename(columns = {"贷款金额":"本机构贷款金额", '贷款余额':"本机构贷款余额"},
          inplace=True)

# 匹配df_out，匹配非本机构的数据
df_results = pd.merge(df_results, df_out, left_on='身份证号码', right_on='证件号码', \
                      how='left')
del df_results['证件号码']
df_results.rename(columns = {"贷款金额":"本机构外贷款金额", '贷款余额':"本机构外贷款余额"},
          inplace=True)

# 匹配df_all，匹配总表的数据
df_results = pd.merge(df_results, df_all, left_on='身份证号码', right_on='证件号码', \
                      how='left')
del df_results['证件号码']
df_results.rename(columns = {"贷款金额":"总贷款金额", '贷款余额':"总贷款余额"},
          inplace=True)

df_results.to_excel(f'd:\\{org_id}.xlsx')

# --------------------------------匹配的结束--------------------------------


# --------------------------------分类统计的开始----------------------------
df_info = pd.DataFrame(columns=['机构','片区','户数','人数合计','0-17岁数',\
                                '18-59岁','60岁以上','曾获得贷款户数(本机构)','累计贷款金额(本机构)',\
                                '当前有余额户数(本机构)','当前贷款余额(本机构)','本支行授信覆盖率',\
                                '本支行用信覆盖率','曾获得贷款户数(非本机构)','累计贷款金额(非本机构)',\
                                '当前有余额户数(非本机构)','当前贷款余额(非本机构)','曾获得贷款的总户数',\
                                '当前有余额户数合计','实际授权覆盖率','实际用信覆盖率'])
    

list_pianqu = list(set(df_results['片区']))
for pianqu in list_pianqu:
    df_tmp = df_results[df_results['片区']==pianqu]
    # 增加'今年','出生年'，'年龄'，以便统计数量
    df_tmp['今年']=datetime.date.today().year
    df_tmp['出生年']=df_tmp['身份证号码'].str[6:10].astype(int)
    df_tmp['年龄']=df_tmp['今年']-df_tmp['出生年']
    df_info.loc[len(df_info.index)] = [org_id,\
                                       pianqu,\
                                       len(df_tmp.groupby('户号',as_index=False)),
                                       len(df_tmp),\
                                       len(df_tmp[df_tmp['年龄'] < 18]),\
                                       len(df_tmp[(df_tmp['年龄'] > 17) & (df_tmp['年龄'] < 60)]),\
                                       len(df_tmp[df_tmp['年龄'] > 59]),\
                                       len(df_tmp[df_tmp['本机构贷款金额']>0]),\
                                       df_tmp[df_tmp['本机构贷款金额']>0]['本机构贷款金额'].sum(),\
                                       len(df_tmp[df_tmp['本机构贷款余额']>0]),\
                                       df_tmp[df_tmp['本机构贷款余额']>0]['本机构贷款余额'].sum(),\
                                       '',\
                                       '',\
                                       len(df_tmp[df_tmp['本机构外贷款金额']>0]),\
                                       df_tmp[df_tmp['本机构外贷款金额']>0]['本机构外贷款金额'].sum(),\
                                       len(df_tmp[df_tmp['本机构外贷款余额']>0]),\
                                       df_tmp[df_tmp['本机构外贷款余额']>0]['本机构外贷款余额'].sum(),\
                                       len(df_tmp[df_tmp['总贷款金额']>0]),\
                                       len(df_tmp[df_tmp['总贷款余额']>0]),\
                                       '',\
                                       '']



