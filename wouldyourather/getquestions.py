#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: getquestions.py 
@time: 2024/04/26
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

import requests
import csv
import os

"""
https://wouldurather.io/api/vote?id=1&option=2 直接用接口 用id区分，最大到 667 这个文件爬这个

https://www.teenvogue.com/story/how-you-answer-these-171-would-you-rather-questions-says-a-lot-about-you 275 个问题

https://www.thebestideasforkids.com/would-you-rather-questions-for-kids/ 孩子
"""


def fetch_data(id_value):
    url = f"https://wouldurather.io/api/vote?id={id_value}&option=2"
    # 本地SOCKS5代理的IP地址和端口
    proxies = {
        'http': 'socks5://127.0.0.1:7890',
        'https': 'socks5://127.0.0.1:7890'
    }

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/58.0.3029.110 Safari/537.3 '
    response = requests.get(url, headers={"User-Agent": user_agent}, proxies=proxies)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None


def save_to_csv(data):
    file_exists = os.path.isfile('would_urather_data_io.csv')  # 检查文件是否存在
    with open('would_urather_data_io.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['option1', 'option2', 'option1Votes', 'option2Votes', 'recommended',
                                                  'active', 'available', 'hidden', 'like', 'dislike'])
        if not file_exists:  # 如果文件不存在，则写入表头
            writer.writeheader()
        writer.writerow({'option1': data['option1'], 'option2': data['option2'], 'option1Votes': data['option1Votes'],
                         'option2Votes': data['option2Votes'], 'recommended': 0,
                         'active': 1, 'available': 1, 'hidden': 0, 'like': 0,
                         'dislike': 0})


def main():
    for id in range(1, 668):
        data = fetch_data(id)
        if data:
            save_to_csv(data)
            print(f"save data id {id} successfully.")
    print("All Data saved successfully.")


if __name__ == "__main__":
    main()
