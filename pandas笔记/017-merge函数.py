"""
merge函数：
拼接两个数据框
"""
import pandas as pd

df_1 = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\8.merge函数\data1.csv",
encoding='gbk',engine='python')
df_2 = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\8.merge函数\data2.csv",
encoding='gbk',engine='python')

#根据name将两个数据框连接起来，删除各自数据框独有的信息
df_3 = pd.merge(df_1, df_2, left_on='name', right_on='name')
#根据name将两个数据框连接起来，保留左边的信息
df_4 = pd.merge(df_1, df_2, left_on='name', right_on='name',
                how='left')
#根据name将两个数据框连接起来，保留右边的信息
df_5 = pd.merge(df_1, df_2, left_on='name', right_on='name',
                how='right')
#根据name将两个数据框连接起来，全部保留
df_6 = pd.merge(df_1, df_2, left_on='name', right_on='name',
                how='outer')






















