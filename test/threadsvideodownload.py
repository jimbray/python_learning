#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: threadsvideodownload.py 
@time: 2023/07/12
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

import requests
from bs4 import BeautifulSoup

# 发送HTTP请求获取网页内容
url = "https://www.threads.net/t/Cuep7olMVZg/?igshid=NTc4MTIwNjQ2YQ%3D%3D"  # 替换为你想要解析的网址
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML文档
soup = BeautifulSoup(html_content, 'html.parser')

# 查找视频标签
video_tags = soup.find_all('video')

# 提取视频下载地址
video_urls = []
for video_tag in video_tags:
    video_url = video_tag['src']
    video_urls.append(video_url)

# 打印视频下载地址
for video_url in video_urls:
    print(video_url)

