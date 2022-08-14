import pandas as pd

dic = {'name':['Kiti', 'Beta', 'Peter', 'Tom'],
       'age':[20, 18, 35, 21],
       'gender':['f', 'f', 'm', 'm']}
df = pd.DataFrame(dic)


"""
根据年龄这一列，进行排序【升序和子降序】
"""
df = df.sort_values(by=['age'])
df = df.sort_values(by=['age'], ascending=False)

"""
值替换
"""
df['gender'] = \
df['gender'].replace(['m', 'f'],['male', 'female'])

"""
重新排列数据中的列
"""
cols = ['name', 'gender', 'age']
df = df.ix[:, cols]
