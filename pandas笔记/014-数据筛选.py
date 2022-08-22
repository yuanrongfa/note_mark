"""
根据一定条件，抽取数据
"""
import pandas as pd

df = pd.read_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\5.数据抽取\data1.csv",
encoding='gbk',engine='python')

"""
比较运算：包含大于、小于等运算
逻辑判断+取数
"""
#抽取好评数大于17000的电脑
df[df['好评数'] > 17000]
#抽取好评数在15000到17000之间的电脑
df[df['好评数'].between(15000, 17000)]

"""
字符匹配
"""
df[df['品牌'].str.contains('苹果',na=False)]
df[df['品牌'].str.contains('苹果',na=True)]

"""
逻辑运算： &（和）、|（或）
"""
#取出价格小于7000，好评大于16000的电脑
df[(df['价格']<7000) & (df['好评数'] > 16000)]
df[(df['价格']<6000) | (df['好评数']>18000)]




















