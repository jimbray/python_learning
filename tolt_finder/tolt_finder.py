#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: tolt_finder.py 
@time: 2024/07/16
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

import requests
from bs4 import BeautifulSoup
import openpyxl
import time
import random


def get_google_search_results(query, num_results=50):
    search_url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"}

    # 设置 SOCKS5 代理
    proxies = {
        'http': f'socks5://127.0.0.1:7890',
        'https': f'socks5://127.0.0.1:7890'
    }

    response = requests.get(search_url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for g in soup.find_all('div', class_='g'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text if g.find('h3') else 'No title'
            results.append({'title': title, 'link': link})
    return results


def save_to_excel(results, filename='results.xlsx'):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Search Results'
    sheet.append(['Title', 'Link'])
    for result in results:
        sheet.append([result['title'], result['link']])
    workbook.save(filename)


def main():
    query = "site:*.tolt.io"
    results = []
    num_results = 50  # 每次爬取的结果数量
    total_searches = 6  # 总共进行6次搜索

    for i in range(total_searches):
        print(f"Fetching results for search {i+1}...")
        partial_results = get_google_search_results(query, num_results)
        results.extend(partial_results)
        time.sleep(random.uniform(10, 30))  # 随机等待10到30秒
        print("get next page")

    save_to_excel(results)
    print("Data saved to results.xlsx")


if __name__ == "__main__":
    main()