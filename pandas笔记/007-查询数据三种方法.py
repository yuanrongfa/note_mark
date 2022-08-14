"""
loc()
iloc()
ix()
"""
import pandas as pd
import numpy as np
#生成指定日期
datas = pd.data_range('20180101', periods=5)
df = pd.DataFrame(
    np.arange(30).reshape(5,6), index=datas,
    columns=['A','B','C','D','E','F'])

"""
loc()方法
df.loc[x, y]
【标签索引】
"""
#打印某个值
df.loc['20180103', 'B']
#打印某列值
df.loc[:,'B']
df.loc['20180103':,'B']
df.loc['20180103':,['B', 'D']]
#打印某些行值
df.loc['20180103':,:]

"""
iloc()方法
"""
#获取某个数据
df.iloc[1,2]
#获取某列
df.iloc[:,2]
#获取某几列
df.iloc[:,[1,3]]
#获取某行
df.iloc[1,:]
#获取某些行
df.iloc[[1,3,4],:]

"""
ix()方法
混合索引
"""
#访问某些元素
df.ix['20180101':'20180103', [2,3]]
#访问某列
df.ix[:,[2]]
#访问某些列
df.ix[:,[2, 4]]
#访问某些行
df.ix[1,:]
#访问某些行
df.ix[[1,3], :]
















