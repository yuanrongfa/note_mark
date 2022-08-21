import pandas as pd

df = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\简单数据分析\1.统计描述\data1.csv",
encoding='gbk',engine='python')

#基本统计数
df.成绩.describe()

#成绩数量
df.成绩.size

#成绩的最大值
df.成绩.max()

#成绩的最小值
df.成绩.min()

#成绩的和
df.成绩.sum()

#成绩的均值
df.成绩.mean()

#成绩的中位数
df.成绩.median()

#成绩的方差
df.成绩.var()

#成绩的标准差
df.成绩.std()

#累计求和
df.成绩.cumsum()

#最大值和最小值的位置
df.成绩.argmin()
df.成绩.argmax()

#求百分位数（排序为30%的数值）
df.成绩.quantile(
        0.3,
        interpolation='nearest')



















