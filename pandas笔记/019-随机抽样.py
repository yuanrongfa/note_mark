"""
随机抽样：
1.按照个数抽样
2.按照比例抽样
"""
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(600).reshape(100,6),
                  columns=['A','B','C','D','E','F'])
print(df)

#设置随机种子
np.random.seed(seed=2)

#按照个数抽样【不放回】
df.sample(n=10)
#按照个数抽样【有放回】
df.sample(n=20,replace=True)

#按照百分比抽样【不放回】
df.sample(frac=0.2)
#按照百分比抽样【有放回】
new_df = df.sample(frac=0.2,replace=True)










































