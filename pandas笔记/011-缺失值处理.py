import pandas as pd

"""
缺失值处理方式：
1.数据补齐 2.删除对应数据行 3.不处理
"""
df = pd.read_csv(r"C:\Users\Administrator\Desktop\new\数据处理\2.缺失值处理\data.csv",
                   encoding='gbk',engine='python')

"""
进行逻辑判断，判定空值所在的位置
"""
na = df.isnull()

"""
找出空值所在的行数据【逻辑判断+取数】
"""
df[na.any(axis=1)]

"""
找出空值所在的列数据
"""
df[na[['gender']].any(axis=1)]
df[na[['age']].any(axis=1)]
df[na[['age', 'gender']].any(axis=1)]

"""
填充缺失值
"""
df1 = df.fillna('1')

"""
删除缺失值【删除整行数据】
"""
df2 = df.dropna()













