#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:jimbray 
@file: calBudget.py 
@time: 2020/11/18
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""
import pandas as pd


# 遇到问题1： 警告：ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex)
# 解决1：https://blog.csdn.net/qth515/article/details/78221771

# 读取 上个月的 sales report
def readPreSalesFile():
    # frame = pd.read_csv("full.csv", 'Previous Month Sales', engine='python')
    frame = pd.read_csv("full.xlsx", 'Previous Month Sales')
    # print(frame[frame['SKU'] == 'MPT54-0056'])
    # print(frame.loc(frame['SKU'] == 'MPT54-0056'))
    # print(frame.loc(1, 'SKU'))
    print(frame)



# 读取 之前的 budget report
def readPreBudgetFile():
    pass


# 生成新的 budget report 文件
def generageResultFile():
    pass


if __name__ == '__main__':
    # 得到 presales 对象
    preSalesFrame = readPreSalesFile()

    # 得到 prebudget 对象

    # 新建一个 budget report 对象

    # 写入 表头

    # 以SKU 为 KEY，遍历 presales 每一行
    # 以SKU 为 KEY, 寻找 prebudget 中的对应的那一行数据
    # 生成 budget report 的每一个 新字段（通过计算）

    # 保存 budget report 为 csv

    pass