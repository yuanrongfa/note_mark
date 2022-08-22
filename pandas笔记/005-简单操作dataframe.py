import pandas as pd

df = pd.DataFrame(
        {'age':[10,11,12],
        'name':['tim', 'tom', 'rose'],
        'income':[100,200,300]},
        index=['person1', 'person2', 'person3'])

"""
修改列名
"""
print(df.columns)
df.columns = range(0, len(df.columns))
print(df.columns)

#精准修改
df.rename(columns = {"age":"年龄", 'name':"姓名"},
          inplace=True)
"""
修改行名
"""
print(df.index)
df.index = range(0,len(df.index))
print(df.index)

"""
增加一列
"""
#在最后添加一列
df['pay'] = [20, 30, 40]
#在任意位置添加一列
df.insert(0, 'pay', df.pop('pay'))


"""
增加一行
"""
df.loc['person4', ['age', 'name', 'income']] \
= [20, 'kitty', 200]

"""
访问DataFrame
"""
#访问某列
df.name
#访问某些列
df[['age', 'name']]
df[[0, 2]]

#访问行
df[0:2]
#使用loc访问
df.loc[['person1', 'person4']]
#访问某个值
df.loc['person1', 'name']

"""
删除
"""
#直接在原数据上删除
del df['age']
#删除列
data = df.drop('name', axis=1, inplace=False)
#删除行
df.drop('person3', axis=0, inplace=True)

#发哥的补充，删除列，不会修改原来的df
df.drop(columns='客户姓名')

#发哥的补充，删除‘客户名称'后，把'贷款余额'转成浮点型，最后求和。
df.drop(columns='客户名称')['贷款余额'].astype(float).sum()


import pandas as pd
import numpy as np


datas = pd.date_range('20180101',periods=5)
df1 = pd.DataFrame(np.arange(30).reshape(5,6),index=datas,columns=['A','B','C','D','E','F'])
print(df1)
print()










