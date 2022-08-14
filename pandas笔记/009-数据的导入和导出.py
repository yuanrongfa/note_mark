"""
读取csv文件
"""
import pandas as pd

df_1 = pd.read_csv(
    r"c:\Uwrs\Administraotr\Desktop\new\数据处理\data1.csv",
    encoding='uft8', engine='python')

df_2 = pd.read_csv(
    r"c:\Uwrs\Administraotr\Desktop\new\数据处理\data2.csv",
    encoding='uft8', engine='python', header=None)

"""
读取excel文件
"""
df_3 = pd.read_excel(
    r"c:\Uwrs\Administraotr\Desktop\new\数据处理\data3.xlsx)
    

df_4 = pd.read_table(
      r"c:\Uwrs\Administraotr\Desktop\new\数据处理\data4.txt",
      sep=',', encoding='uft8', engine='python', header=None)



"""
导出文件
"""
df_1.to_csv(
      r"c:\Uwrs\Administraotr\Desktop\new\数据处理\导出.csv",
      index=True, header=True)

df_1.to_excel(
      r"c:\Uwrs\Administraotr\Desktop\new\数据处理\导出.xlsx",
      index=True, header=True)

"""
编码:
utf-8:包含全世界所有国家需要用到的字符，英文网站用的较多
gbk:包含全部的中文字符。
unicode:把所有语言统一到一套编码。









