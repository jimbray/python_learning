#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:jimbray 
@file: generaQRCode.py 
@time: 2018/12/29
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Description: 生成二维码，目前种类
1. 单纯二维码
2. 图片背景二维码
2. 图片带颜色二维码 -c 0 为带颜色，其他为无色
"""

from MyQR import myqr
import argparse

url = "http://jimbray.xyz"

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-c', '--color')

args = parser.parse_args()

IMG = args.file

WITH_COLOR = args.color

if __name__ == '__main__':
    if IMG is not None:
        print(WITH_COLOR)
        myqr.run(
            words=url,
            picture=IMG,
            colorized=(WITH_COLOR == '0')
        )
    else:
        myqr.run(url)