#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: hf_weather.py 
@time: 2022/03/08
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""
import requests


def get_weather():
    base_url = "https://devapi.qweather.com/v7/indices/1d"
    # 深圳ID，通过https://geoapi.qweather.com/v2/city/top?number=10&range=cn&key=c1599639af99455fa82488aac62c087d 获取
    location = "101280601"
    # 天气指数类型：https://dev.qweather.com/docs/resource/indices-info/
    type = "1,2,3,5,8,10,13,14,15,16"

    # get url 操作
    url = base_url + "?location=" + location + "&type=" + type + "&key=c1599639af99455fa82488aac62c087d"
    # print(url)
    # 获取数据
    response = requests.get(url)
    # 获取数据
    data = response.json()
    daily_data = data['daily']
    date = daily_data[0]['date']
    result_str = "日期：" + date + "\n"
    simple_result_str = "日期：" + date + "\n"
    for i in range(0, len(daily_data)):
        result_str = result_str + daily_data[i]['name'] + "：" + str(daily_data[i]['category']) + "\n" + daily_data[i][
            'text'] + "\n"

    for i in range(0, len(daily_data)):
        simple_result_str = simple_result_str + daily_data[i]['name'] + "：" + str(daily_data[i]['category']) + "\n"

    return result_str, simple_result_str


def sendWeather(result, simple_result):
    base_url = "https://cloud-dev-4d6931-1252086379.ap-shanghai.app.tcloudbase.com/push_all"
    result_url = base_url + "?content=" + result
    simple_result_url = base_url + "?content=" + simple_result
    requests.get(result_url)
    requests.get(simple_result_url)


if __name__ == '__main__':
    result, simple_result = get_weather()
    sendWeather(result, simple_result)
