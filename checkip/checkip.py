#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: checkip.py 
@time: 2022/12/08
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""
# 导入所需的库
from flask import Flask, request
import requests

# 定义网络服务
app = Flask(__name__)

# 定义路由，获取用户访问的代理 IP 地址
@app.route("/proxy")
def get_proxy_ip():
    try:
        # 获取中国大陆 IP 地址
        # china_ip_resp = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip=myip").json()
        # print("china: ", china_ip_resp)
        # china_ip = china_ip_resp["data"]["ip"]

        # 获取普通国外 IP 地址
        foreign_ip_resp = requests.get("https://api.ipify.org?format=json").json()
        print("foreign:" , foreign_ip_resp)
        foreign_ip = foreign_ip_resp["ip"]

        # 获取 Google IP 地址
        google_ip_resp = requests.get("https://www.google.com/search?q=59.82.84.20").text
        print("google: ", google_ip_resp)
        google_ip = google_ip_resp.split("\n")[2].strip()

        # 返回不同地区的代理 IP 地址
        return f"中国大陆 IP 地址：普通国外 IP 地址：{foreign_ip}\nGoogle IP 地址：{google_ip}"
    except:
        return "无法获取代理 IP 地址，请稍后重试"

# 启动服务
app.run()

