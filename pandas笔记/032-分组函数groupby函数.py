import pandas as pd
import numpy as np

df = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\简单数据分析\2.分组统计groupby函数\data1.csv",
encoding='gbk',engine='python')

"""
groupby()函数
"""
result1 = df.groupby(by=['班级'])['成绩'].agg(
        {"总分":np.sum,
         "人数":np.size,
         "平均成绩":np.mean,
         "标准差":np.std})

#自定义分组
bins = [min(df.成绩)-1, 70, 80, 90, max(df.成绩)+1]
labels = ['70以下', '71~80', '81~90', '90以上']
df['分组'] = pd.cut(df.成绩, bins, labels=labels)
#根据自定义分组进行分组统计
result2 = df.groupby(by=['分组'])['成绩'].agg(
        {"总分":np.sum,
         "人数":np.size,
         "平均成绩":np.mean,
         "标准差":np.std})






















