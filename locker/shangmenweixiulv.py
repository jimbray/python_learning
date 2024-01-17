#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: clean.py
@time: 2024/01/17
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions:
"""
## 上门维修率分析

# 计算每个月的工单总数。
# 计算每个月完成上门的工单数量。 （解决方案(安装师傅)列不为空）
# 计算上门维修率（完成上门的工单数量 / 总工单数）。

import pandas as pd


# 清理没有相关的数据列
def cleanData():
    print("清理列数据开始")
    # 读取原始 Excel 文件
    file_path = 'data.xlsx'  # 请替换为您的文件路径
    df = pd.read_excel(file_path, engine='openpyxl')

    # 保留必要的列
    columns_to_keep = ['工单编号', '工单状态', '工单创建时间', '解决方案(安装师傅)']
    df_cleaned = df[columns_to_keep]

    # 保存清理后的数据到新文件
    cleaned_file_path = 'cleaned_data.xlsx'  # 新文件的路径
    df_cleaned.to_excel(cleaned_file_path, index=False, engine='openpyxl')

    print("数据清理完成，文件已保存为:", cleaned_file_path)

    return cleaned_file_path


# 清理 【解决方案(安装师傅)】列为空的数据
# 不能清理掉这个数据，会影响 总单数
# def cleanNull(cleaned_file_path):
#     print("清理【解决方案-安装师傅】列为空的数据")
#     # 读取清理后的数据
#     df = pd.read_excel(cleaned_file_path, engine='openpyxl')
#
#     # 删除【解决方案(安装师傅)】列为空的行
#     df = df[df['解决方案(安装师傅)'].notna()]
#
#     # 保存进一步清理后的数据
#     further_cleaned_file_path = 'further_cleaned_data.xlsx'
#     df.to_excel(further_cleaned_file_path, index=False, engine='openpyxl')
#
#     print("清理空值数据完成，文件已保存为:", further_cleaned_file_path)
#
#     return further_cleaned_file_path


# 计算剩余数据的行数
def calRemainedRows(further_cleaned_file_path):
    print("计算剩余数据行数开始")

    # 读取经过进一步清理后的数据
    df = pd.read_excel(further_cleaned_file_path, engine='openpyxl')

    # 计算并打印行数
    row_count = len(df)
    print("剩余数据的行数为:", row_count)

    return row_count


def start():
    print("开始执行分析")

    # 清理数据
    # cleaned_file_path = cleanData()

    cleaned_file_path = 'cleaned_data.xlsx'
    # 清理空数据
    # further_cleaned_file_path = cleanNull(cleaned_file_path)

    # 计算数据剩余行数
    remained_rows = calRemainedRows(cleaned_file_path)

    print("最终剩余数据的行数为：", remained_rows, "行")


if __name__ == '__main__':
    start()
