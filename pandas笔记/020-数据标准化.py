import pandas as pd

"""
数据标准化的方式：
1.0~1标准化：也称离差标准化，它是对原始数据进行线性变换，
使结果落到 [0,1] 区间.
X=(x - min)/(max - min)
2.Z标准化:数据均值为0，方差为1.
X=(x - mean)/std

标准化原因：消除量纲的影响
"""
df1 = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\11.数据标准化\data1.csv",
encoding='gbk',engine='python')

df1.columns
#0~1标准化
df1['国内生产总值0~1标准化'] = \
   round((df1.国内生产总值 - df1.国内生产总值.min())
   /(df1.国内生产总值.max()-df1.国内生产总值.min()),2)

df1['人均GDP 0~1标准化'] = \
   round((df1.人均GDP - df1.人均GDP.min())
   /(df1.人均GDP.max()-df1.人均GDP.min()),2)

#分析相关性
df1['人均GDP 0~1标准化'].corr(df1['国内生产总值0~1标准化'])

#Z标准化
df1['国内生产总值Z标准化'] = \
   round((df1.国内生产总值 - df1.国内生产总值.mean())
   /(df1.国内生产总值.std()),2)

df1['人均GDP Z标准化'] = \
   round((df1.人均GDP - df1.人均GDP.mean())
   /(df1.人均GDP.std()),2)
   
df1['国内生产总值Z标准化'].mean()
df1['国内生产总值Z标准化'].std()

df1['人均GDP Z标准化'].mean()
df1['人均GDP Z标准化'].std()


df1['国内生产总值Z标准化'].corr(df1['人均GDP Z标准化'])











