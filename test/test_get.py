#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: test_get.py 
@time: 2021/11/17
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

import requests


def get_operation():
    msg_text = "任务通知：今天把 dailyceckin 和 JD_scripts 的cookies都更新一下吧"
    url = 'https://cloud-dev-4d6931-1252086379.ap-shanghai.app.tcloudbase.com/push?content=' + msg_text
    result = requests.get(url)
    print(result.text + ' : ' + msg_text)


if __name__ == '__main__':
    get_operation()
