# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import datetime
import openpyxl


file = r'd:\a2.xlsx'
wb = openpyxl.load_workbook(file)
sh = wb.active
i_rows = sh.max_row #最大记录数后一行空白处


sh.cell(i_rows + 1,3).value = f'=sum(c2:c{i_rows})'     # 户数
sh.cell(i_rows + 1,4).value = f'=sum(d2:d{i_rows})'     # 人数合计
sh.cell(i_rows + 1,5).value = f'=sum(e2:e{i_rows})'     # 0-17岁
sh.cell(i_rows + 1,6).value = f'=sum(f2:f{i_rows})'     # 18-59岁
sh.cell(i_rows + 1,7).value = f'=sum(g2:g{i_rows})'     # 60岁以上
sh.cell(i_rows + 1,8).value = f'=sum(h2:h{i_rows})'     # 曾获得贷款户数(本机构)
sh.cell(i_rows + 1,9).value = f'=sum(i2:i{i_rows})'     # 累计贷款金额(本机构)
sh.cell(i_rows + 1,10).value = f'=sum(j2:j{i_rows})'    # 当前有余额户数(本机构)
sh.cell(i_rows + 1,11).value = f'=sum(k2:k{i_rows})'    # 当前贷款余额(本机构)
sh.cell(i_rows + 1,14).value = f'=sum(n2:n{i_rows})'    # 曾获得贷款户数(非本机构)
sh.cell(i_rows + 1,15).value = f'=sum(o2:o{i_rows})'    # 累计贷款金额(非本机构)
sh.cell(i_rows + 1,16).value = f'=sum(p2:p{i_rows})'    # 当前有余额户数(非本机构)
sh.cell(i_rows + 1,17).value = f'=sum(q2:q{i_rows})'    # 当前贷款余额(非本机构)
sh.cell(i_rows + 1,18).value = f'=sum(r2:r{i_rows})'    # 曾获得贷款的总户数
sh.cell(i_rows + 1,19).value = f'=sum(s2:s{i_rows})'    # 当前有余额户数合计

for i in range(2,i_rows + 2): # 默认i从0开始，最后一位不算，所以要加2
    sh.cell(i,12).value = f'=h{i} / c{i}' # 本支行授信覆盖率
    sh.cell(i,12).number_format = '0.00%'
    
    sh.cell(i,13).value = f'=j{i} / c{i}' # 本支行用信覆盖率
    sh.cell(i,13).number_format = '0.00%'  
    
    sh.cell(i,20).value = f'=r{i} / c{i}' # 实际授权覆盖率
    sh.cell(i,20).number_format = '0.00%'     

    sh.cell(i,21).value = f'=s{i} / c{i}' # 实际用信覆盖率
    sh.cell(i,21).number_format = '0.00%'    
    
wb.save(r'd:\aa.xlsx')

print(sh.min_row)
print(sh.max_row)

    