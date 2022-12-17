"""
2022-12-16
该程序用于处理那种电子表格中明明是字条串，
但是复制出来后前后会有双引号和TAB符号的问题
"""
# 以下两个是用于选择文件窗口的库
import tkinter as tk
from tkinter import filedialog

import pandas as pd

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

# Folderpath = filedialog.askdirectory() #获得选择好的文件夹
Filepath = filedialog.askopenfilename() #获得选择好的文件

# 把文件路径（含文件名）分割后，最后一个list为文件名
Filename = Filepath.split('/')[-1]

# 把文件路径（含文件名）分割后，去掉文件名后，就为文件目录
Folderpath = Filepath.rstrip(Filename)


# 打开xlsx文件
df=pd.read_excel(Filepath,dtype=str)


# print(type(list(df.columns)))


for lis_tmp in list(df.columns):
    
    print('正在处理%s...\n'%(lis_tmp))
    
    df[lis_tmp]=df[lis_tmp].str.replace(r'\t','',regex=True)
    
print('处理结束，正在导出文件...')

df.to_excel(Folderpath + '格式调整后-' + Filename,index=False)

print('文件导出完成!')
