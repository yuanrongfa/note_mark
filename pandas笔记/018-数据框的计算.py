import pandas as pd

df = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\9.计算\data1.csv",
encoding='gbk',engine='python')

df['总价'] = df['单价'] * df['数量']
df.总价 = df['单价'] * df['数量']
df.单价 * 2







































