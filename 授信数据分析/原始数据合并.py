'''
合并list下所有的.xlsx文件，并把‘户籍.xlsx’输出来list_out文件夹中。
'''


import pandas as pd

import os

if datetime.date.today().year > 2023:
    print('程序需要更新库文件!')
    exit()

print('提示：需要用到【list】、【list_out】文件夹。\n \n')

# 当前程序目录必须要创建一个list文件夹，用于存在每个机构的原始数据，用于合并。
path = os.path.abspath('./list/')

list_tmp = os.listdir(path)

df_new = pd.DataFrame()


for list_i in list_tmp:
    # 如果只有一个表，就无必要合并了
    if len(list_tmp) > 1:
        
        print('正在合并:' + list_i)
        
        df = pd.read_excel(path +'//'  + list_i )
        
        df_new = pd.concat([df_new,df],ignore_index=True)
        
        # print(df)
    
    else:
        
        print('必须要有两个以上的机构才能合并！')

#print(df_new)

print('正在生成户籍总表...')
df_new.to_excel('.//list_out//户籍.xlsx',index=False)

temps = input('数据合并完成,按回车键退出程序，版权归田阳农商行业务拓展部所有。\n')