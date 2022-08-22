"""
读取csv文件
"""
import pandas as pd

df_1 = pd.read_csv(
        r"C:\Users\Administrator\Desktop\new\数据处理\1. 数据导入与导出\data1.csv",
        encoding='utf8', engine='python')

df_2 = pd.read_csv(
        r"C:\Users\Administrator\Desktop\new\数据处理\1. 数据导入与导出\data2.csv",
        encoding='utf8', engine='python',header=None)

"""
读取excel文件
"""
df_3 = pd.read_excel(
        r"C:\Users\Administrator\Desktop\new\数据处理\1. 数据导入与导出\data3.xlsx",)

"""
读取txt文件
"""
df_4 = pd.read_table(
        r"C:\Users\Administrator\Desktop\new\数据处理\1. 数据导入与导出\data4.txt",
        sep=',', engine='python',header=None)

"""
导出文件
"""
df_1.to_csv(
r"C:\Users\Administrator\Desktop\new\数据处理\1. 数据导入与导出\导出.csv",
index=True, header=True)

df_1.to_excel(
r"C:\Users\Administrator\Desktop\new\数据处理\1. 数据导入与导出\导出.xlsx",
index=True, header=True)

"""
编码：
utf-8:包含全世界所有国家需要用到的字符，英文网站用的较多
gbk:包含全部的中文字符。
unicode:把所有语言统一到一套编码。
"""
















































