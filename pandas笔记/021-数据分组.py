"""
cut()函数：
cut(Series, bins, right=True, labels=null)
Series:需要分组的数据【数据框的某列数据】
bins:分组的划分数组【列表】
right:分组的时候，右边是否闭合。默认闭区间。
labels:分组的自定义标签。
"""
import pandas as pd

df = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\12.数据分组\data1.csv",
encoding='gbk',engine='python')

#对人均GDP进行分组
bins = [min(df.人均GDP)-1, 2000, 4000, 6000, 8000, max(df.人均GDP)+1]
df['人均GDP分组'] = pd.cut(df.人均GDP, bins)
df['人均GDP分组'] = pd.cut(df.人均GDP, bins, right=False)

#自定义标签
labels = ['2000以下', '2001~4000', '4001~6000', '6001~8000', '8000以上']
df['人均GDP分组'] = pd.cut(df.人均GDP, bins, labels=labels)












