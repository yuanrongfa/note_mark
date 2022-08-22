import pandas as pd

df = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\13.时间格式数据\data1.csv",
encoding='gbk',engine='python')

"""
to_datetime()函数：
to_datetime(Series, format)
Series:字符型时间数据；【数据框的时间那一列】
format:格式化的方法
"""
#将字符型时间数据转化为时间格式数据
df['时间'] = pd.to_datetime(df.购买时间, format='%Y/%m/%d')

#将时间格式的数据转化为指定字符型数据
df['字符型时间'] = df.时间.dt.strftime('%Y/%m/%d')

#提取时间格式数据中的年、月、周、日、时、分、秒
df['年'] = df['时间'].dt.year
df['月'] = df['时间'].dt.month
df['周'] = df['时间'].dt.weekday
df['日'] = df['时间'].dt.day
df['时'] = df['时间'].dt.hour
df['分'] = df['时间'].dt.minute
df['秒'] = df['时间'].dt.second



































