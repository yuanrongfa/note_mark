# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

file =r'/Users/yuan/list/a1.xlsx'

df = pd.read_excel(file,header=0)


# 记录总条数
i=df[df['类别']=='硬盘']['收入'].size
print(i)


# 收入统计总数
df[df['类别']=='硬盘']['收入'].sum()

# 分类统计价格总数
df.groupby('类别').get_group('硬盘')['收入'].sum()
