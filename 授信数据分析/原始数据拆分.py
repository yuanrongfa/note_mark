'''
总户籍表放到in文件夹中，处理完分割后，把它输入到list_out中。
copyright@2022-10-16
'''

# -*- coding: utf-8 -*-

import pandas as pd

import os

if datetime.date.today().year > 2023:
    print('程序需要更新库文件!')
    exit()

path = os.path.abspath('./in/户籍.xlsx')

# path = os.path.abspath('d:/in/户籍.xlsx')

print('提示：需要用到【in】、【org_out】文件夹。\n \n')

# 机构号转支行名称
org_id_to_name = {'6066':'营业部', \
                  '6067':'田州支行', \
                  '6069':'阳光支行', \
                  '6104':'鑫茂支行', \
                  '6100':'银丰支行', \
                  '6068':'古城支行', \
                  '6070':'三雷支行', \
                  '6090':'百育支行', \
                  '6088':'那满支行', \
                  '6097':'头塘支行', \
                  '6098':'二塘支行', \
                  '6071':'那坡支行', \
                  '6073':'百峰支行', \
                  '6076':'坡洪支行', \
                  '6085':'五村支行', \
                  '6079':'洞靖支行', \
                  '6081':'桥业支行', \
                  '6083':'巴别支行', \
                  '6093':'玉凤支行', \
                  '6095':'坤平支行'}

print('正在读取总户籍，内容比较多，请稍候几分钟...')
df = pd.read_excel(path)

list_org_id = list(set(df['机构']))


# org_id = 6093

for org_id in list_org_id:
    
    
    df_new = df[df['机构']==org_id]
    
    df_new['户号']=df_new['户号'].astype(str)
    
    df_new['机构']=df['机构'].astype(str)
    
    print('正在保存：' + org_id_to_name[str(org_id)] + '...')
    
    df_new.to_excel('.//org_out//' + org_id_to_name[str(org_id)] + '.xlsx',index=False)

temps = input('处理完成,按回车键退出程序，版权归田阳农商行业务拓展部所有。\n')