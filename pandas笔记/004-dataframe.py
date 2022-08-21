"""
DataFrame(数据框)
就是excel表（多个Series的拼接）
"""
import pandas as pd

df_1 = pd.DataFrame({'age':[10,11,12],
                     'name':['tim', 'tom', 'rose'],
                     'income':[100,200,300]},
                     index=['person1', 'person2', 'person3'])
print(df_1)

"""
dataframe的属性
"""
#行索引
df_1.index
#列名
df_1.columns
#值
df_1.values

df_1 = pd.DataFrame({'age':[10,11,12],
                     'name':['tim', 'tom', 'rose'],
                     'income':[100,200,300]})
print(df_1)




































