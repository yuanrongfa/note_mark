
import pandas as pd

df = pd.read_excel(
r"C:\Users\Administrator\Desktop\new\简单数据分析\4.相关分析\data1.xlsx",
encoding='gbk')

df.columns

#计算两列之间的相关性
df['人均GDP(元)'].corr(df['人均消费水平（元）'])

#计算相关系数矩阵
z = df[['人均GDP(元)', '人均消费水平（元）']].corr()
print(z)

















