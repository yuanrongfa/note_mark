"""
slice()函数：
字段截取函数，作用对象是字符串
身份证：
前6位：地址码
接着8位：出生日期码
再3位：顺序码
最后1位：校验码
"""
import pandas as pd

df = pd.read_csv(r"C:\Users\Administrator\Desktop\new\数据处理\4.slice函数的使用\data1.csv",
                   encoding='gbk',engine='python')
"""
将id转化为字符串
"""
df['id'] = df['id'].astype(str)

"""
提取地址码(前6位)
"""
#area = df['id'].slice(0,6)
area = df['id'].str.slice(0,6)

"""
提取出生日期码（接着8位）
"""
birthday = df['id'].str.slice(6,14)

"""
提取顺序码（接着3位）
"""
ranking = df['id'].str.slice(14,17)

"""
提取唯一校验码
"""
only = df['id'].str.slice(17,18)

"""
将信息添加回数据框
"""
df['area'] = area
df['birthday'] = birthday
df['ranking'] = ranking
df['only'] = only





















































