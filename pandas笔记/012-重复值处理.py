import pandas as pd


df = pd.read_csv(r"C:\Users\Administrator\Desktop\new\数据处理\3.重复值处理\data1.csv",
                   encoding='gbk',engine='python')

"""
找出重复值的位置【逻辑判断】
"""
result1 = df.duplicated()

"""
根据列名来判断重复
"""
#根据某个
result2 = df.duplicated('gender')
print(result2)

#根据某些
result3 = df.duplicated(['gender', 'name'])
print(result3)

"""
提取重复的行
"""
df[result1]
df[result2]
df[result3]

"""
删除重复的行
"""
#完全重复
new_df1 = df.drop_duplicates()

#部分重复【根据某列名来删除】
new_df2 = df.drop_duplicates(['name', 'gender'])
print(new_df2)




































