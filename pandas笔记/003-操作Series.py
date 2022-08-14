"""
Created on Sun Aug 14 20:49:29 2022

@author: yuan
"""

import pandas as pd

S-1 = pd.Series([1,2,3,4,5],
                index=['a','b','c','d','e'])

s_2 = pd.Series(['Lily','Rose','Jack'])


#查
"""
(1)通过标签访问
"""
#访问某个元素
s_1['d']
#访问多个元素[Series的切片]
s_1['a':'d']
#访问多个元素
s_1[['a','d']]

"""
(2)通过索引访问
"""
s_2[0]
s_2[0:2]
s_2[[0,2]]

s_1[4]

#增
#s_2.append('2')
s_3 = pd.Series(['2'], index=['d'])
s_2 = s_2.append(s_3)
#s_2.indert(1, s_3)

#删除
s_1 = s_1.drop('a')
#判断一下某个值是否在Series里面
print('jim' != s_2.values)

#改
s_2[0] = 'Peter'
s_2[[0,3]] = 'Tom'

#创建Series
dic_1 = {'name1':'Perter','name':'Tim',
         'name3':'Rose'}
s_4 = pd.Series(dic_1)
print(s_4)

#重置索引
s_4.index = range(0, len(s_4))
































