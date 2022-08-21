""" 
Series:(系列)
可以看做竖起来的list
"""
import pandas as pd

#生成第一个Series[按照默认的index]
s_1 = pd.Series([1,2,3,4,5])
print(s_1)

#自定义index
s_2 = pd.Series([1,2,3,4,5], 
                index=['a', 'b', 'c', 'd', 'e'])
print(s_2)

s_3 = pd.Series(['Lily', "Rose", "Jack"])
print(s_3)

#Series的一些属性
s_1.index
s_2.index
s_1.values
s_3.values


































































