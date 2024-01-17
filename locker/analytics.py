#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: analytics.py 
@time: 2024/01/17
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

## 上门维修率

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.font_manager import FontProperties

# 设置中文显示字体
font = FontProperties(fname='yong.ttf', size=14) # 替换为您的中文字体文件路径

print("开始读取 Excel 文件...")
# 读取 Excel 文件，使用 openpyxl 引擎
df = pd.read_excel('data.xlsx', engine='openpyxl')
print("文件读取完成。")

print("正在处理数据...")
# 确保日期列被正确解析
df['工单创建时间'] = pd.to_datetime(df['工单创建时间'])

# 检查“解决方案(安装师傅)”列非空的记录，作为完成上门维修的判定
df['上门维修完成'] = df['解决方案(安装师傅)'].notna()

# 以月为单位分组，计算每月的工单总数和完成上门维修的工单数
monthly_data = df.groupby(df['工单创建时间'].dt.to_period('M')).agg(
    总工单数=('工单编号', 'count'),
    完成上门维修工单数=('上门维修完成', 'sum')
)

# 计算上门维修率
monthly_data['上门维修率'] = monthly_data['完成上门维修工单数'] / monthly_data['总工单数']
print("数据处理完成。")

print("正在生成图表...")
# 绘制折线图
fig, ax = plt.subplots()
monthly_data['上门维修率'].plot(kind='line', marker='o', ax=ax)

# 设置图表标题和坐标轴标签，使用中文
ax.set_title('每月上门维修率', fontproperties=font)
ax.set_xlabel('月份', fontproperties=font)
ax.set_ylabel('上门维修率', fontproperties=font)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax.xaxis.set_major_locator(mdates.MonthLocator())

plt.xticks(rotation=45)

plt.grid(True)
plt.show()
print("图表生成完毕。")
