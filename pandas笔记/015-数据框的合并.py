"""
concat()函数：
使用方式：concat([df1,df2,df3...])
"""
import pandas as pd
import numpy as np

df_1 = pd.DataFrame(np.arange(12).reshape(3,4))
df_2 = 2*df_1

#竖向合并
new_df1 = pd.concat([df_2, df_1])
#横向合并
new_df2 = pd.concat([df_1, df_2], axis=1)

"""
join参数 inner:表示交集 outer:表示并集
"""
df_3 = pd.DataFrame(np.arange(12).reshape(3,4),
                    index=['A', 'B', 2])
new_df3 = pd.concat([df_1, df_3], axis=1, join='inner')
new_df4 = pd.concat([df_1, df_3], axis=1, join='outer')
































