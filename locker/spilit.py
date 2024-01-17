#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: spilit.py 
@time: 2024/01/17
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""
import pandas as pd

# 定义每个文件的行数限制
rows_per_file = 60000

print("开始读取 Excel 文件...")
# 读取原始 Excel 文件，使用 openpyxl 引擎
df = pd.read_excel('data.xlsx', engine='openpyxl')
print("文件读取完成。")

# 计算需要分割成多少个文件
num_files = len(df) // rows_per_file + int(len(df) % rows_per_file != 0)

# 分割并保存文件
for i in range(num_files):
    start_row = i * rows_per_file
    end_row = start_row + rows_per_file
    df_subset = df.iloc[start_row:end_row]

    # 构造新文件名
    new_filename = f'data-{i + 1}.xlsx'
    df_subset.to_excel(new_filename, index=False, engine='openpyxl')
    print(f'文件 {new_filename} 已保存。')

print("所有文件分割完成。")

