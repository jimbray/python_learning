#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:jimbray
@file: market_interest_rates_tracker.py
@time: 2021/12/24
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions:
"""
import requests
import json
import pandas as pd


def getShibor():
    url = 'https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/shibor/shibor.json'
    res = requests.get(url)
    res.encoding = 'utf-8'
    json_str = res.text
    json_obj = json.loads(json_str)
    shibor = json_obj['records'][7]['shibor']
    return shibor


def getChinaBond():
    url = 'https://yield.chinabond.com.cn/cbweb-mn/yc/ycDetail?ycDefIds=2c9081e50a2f9606010a3068cae70001&&zblx=txy&&workTime=&&dxbj=&&qxlx=&&yqqxN=&&yqqxK=&&wrjxCBFlag=0&locale=zh_CN'
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # referer = 'https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=zh_CN'
    # headers = {'User-Agent': user_agent, 'Referer': referer}

    res = requests.post(url)
    tables = pd.read_html(res.text)
    # 第二个表是目标
    table = tables[1]
    chinabond = table[1][12]
    return chinabond


def pushMsg(shibor, chinabond):
    print("shibor: %s | chinabond: %s" % (shibor, chinabond))

    if shibor is None:
        shibor = '未获取到'
    else:
        shibor = shibor + "%"
    if chinabond is None:
        chinabond = '未获取到'
    else:
        chinabond = chinabond + "%"

    url = 'http://www.pushplus.plus/send'
    data = {
        'token': 'b1c8ebed2c3d4d998fb5404f59f304fa',
        'title': "今日市场利率",
        # 'content': "今日更新</br>Shibor： {}</br>10年期国债到期收益率：{}".format(shibor, chinabond),
        'content': "<div  id='write'  class = 'is-node'><p>今日利率</p><p>Shibor: <strong>{}</strong></p><p>10年期国债到期收益率： <strong>{}</strong></p></div>".format(shibor, chinabond),
        'template': 'html',
        'topic': 'rate',
        'channel': 'wechat'
    }
    # print(url)
    # print(content)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, headers=headers, data=json.dumps(data))
    print(res.text)


if __name__ == "__main__":
    shibor = getShibor()
    chinabond = getChinaBond()
    pushMsg(shibor, chinabond)
