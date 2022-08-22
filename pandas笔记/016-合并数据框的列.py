import pandas as pd

df = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\7.合并数据框的列\data1.csv",
encoding='gbk',engine='python')

"""
使用 + 进行拼接即可
"""
df.columns
num = df['area'] + df['birthday'] + \
        df['ranking'] + df['only'] 
df['id'] = num

df = df.astype(str)
num = df['area'] + df['birthday'] + \
        df['ranking'] + df['only'] 
df['id'] = num
















