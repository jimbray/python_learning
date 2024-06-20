#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:jimbray
@file: sniffer.py
@time: 2024/06/20
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions:
"""


没有成功
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

proxies = {
  "http": None,
  "https": None,
}


def extract_video_url(url):
    # 使用Chrome浏览器驱动
    driver = webdriver.Chrome()
    driver.get(url)

    # 等待页面加载完成
    # 这里可能需要根据实际情况调整等待时间或使用显式等待
    # time.sleep(5)

    # 获取页面源码
    html = driver.page_source
    driver.quit()

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, 'html.parser')

    print(html)

    # 查找视频源地址
    video_source = soup.find('source', src=lambda x: x and x.startswith('//www.douyin.com/'))
    # video_sources = soup.find_all('source', src=lambda x: x and x.startswith('//www.douyin.com/'))
    if video_source:
        # 提取src属性中的URL，并添加https前缀
        video_url = 'https:' + video_source['src']
        return video_url
    else:
        return None


if __name__ == "__main__":
    url = 'https://www.douyin.com/video/7380746833477307711'  # 替换为实际的抖音视频链接
    # print(args[])
    video_url = extract_video_url(url)
    if video_url:
        print("视频URL:", video_url)
    else:
        print("未找到视频URL")