'''
用于表格连续相同的处理。

	序号	姓名	成绩
0	1	袁荣发	101
1	2	袁荣发	102
3	4	袁荣发	104
4	5	袁荣发	105
5	6	袁荣发	106
2	3	韦荣柳	103
6	7	韦荣柳	107
7	8	韦荣柳	108
8	9	韦荣柳	109
9	10	韦荣柳	110
-----------------------------------
[0, 1]
[2]
[3, 4, 5]
[6, 7, 8, 9]
----------------------------------


通过双游标的方法实现，把相同的index加入到列表，然后通过index就可以定位到指定的df.loc
i为第一个游标，j为第二个游标
'''


import pandas as pd

file = r"C:\Users\HiWin11\Desktop\20220830\头塘街.xlsx"

df = pd.read_excel(file)

i = 0

while i < len(df):
    
    b = True
    
    list_tmp = []
    
    j = i 
    
    while b:
        
        if j < len(df):
            
            if df.loc[i,'户主姓名'] == df.loc[j,'户主姓名']:
                
                list_tmp.append(j)
                
                j = j + 1
                
            else:
                
                b = False
                
                i = j
                
                # 以下是后期处理的核心位置
                #print(list_tmp)
                
                name_huZhu = ''
                name_id = ''
                # 第一次for循环，用于查找户主是否存在 ，如果否，则把第一记录作为户主
                for index_x in list_tmp:
                    
                    if df.loc[index_x,'户主姓名']==df.loc[index_x,'姓名']:
                        
                        name_huZhu = df.loc[index_x,'姓名']
                        
                        name_id = df.loc[index_x,'身份证号码']
                        
                        break
                    
                    else:
                        
                        name_huZhu = df.loc[list_tmp[0],'姓名']
                        
                        name_id = df.loc[list_tmp[0],'身份证号码']
                        
                for index_x in list_tmp:
                    
                    df.loc[index_x,'户主姓名'] = name_huZhu
                    
                    df.loc[index_x,'户号'] = name_id
                        
   
        # 这个else用于记录最后一条不输入的补充  
        else:
            
            i = j
            
            b = False
            
            # 以下是后期处理的核心位置
            #print(list_tmp)
            
            name_huZhu = ''
            name_id = ''
            
            for index_x in list_tmp:
                
                if df.loc[index_x,'户主姓名']==df.loc[index_x,'姓名']:
                    
                    name_huZhu = df.loc[index_x,'姓名']
                    
                    name_id = df.loc[index_x,'身份证号码']
                    
                    break
                
                else:
                    
                    name_huZhu = df.loc[list_tmp[0],'姓名']
                    
                    name_id = df.loc[list_tmp[0],'身份证号码']
                    
            for index_x in list_tmp:
                
                df.loc[index_x,'户主姓名'] = name_huZhu
                
                df.loc[index_x,'户号'] = name_id


df.to_excel(r'C:\Users\HiWin11\Desktop\20220830\头塘街--已处理.xlsx',index=False)

