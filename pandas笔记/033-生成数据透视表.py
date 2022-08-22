import pandas as pd
import numpy as np

df = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\简单数据分析\3.生成数据透视表\data1.csv",
encoding='gbk',engine='python')

#自定义分组
bins = [min(df.成绩) - 1, 70, 80, 90, max(df.成绩)+1]
labels = ['70以下', '71~80', '81~90', '90以上']
df['分组'] = pd.cut(df.成绩, bins, labels = labels)

"""
pivot_table(values, index, columns, aggfunc)
values:定义数据透视表中得值【成绩】
index:定义数据透视表中的行【分组】
columns:定义数据透视表中的列【性别】
aggfunc:定义数据透视表的函数【统计人数np.size】
"""
result = df.pivot_table(values=['成绩'],
                        index=['分组'],
                        columns=['性别'],
                        aggfunc=[np.mean])






























