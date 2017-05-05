#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/4/10
__author__ = 'jimbray'

import requests
import json

if __name__ == '__main__':
    url = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101280601'
    jsonStr = requests.get(url).text

    data = json.loads(jsonStr)
    weather = data['data']

    city = weather['city']
    ganmao = weather['ganmao']
    wendu = weather['wendu']
    forecast = weather['forecast']

    today = forecast[0]

    fengli_today = today['fengli']
    fengxiang_today = today['fengxiang']
    high_temp_today = today['high']
    low_temp_today = today['low']
    type_today = today['type']

    weather_str = city + '\n' + ganmao + '\n' + wendu + '\n' + fengli_today + '\n' + fengxiang_today + '\n' +high_temp_today + '\n' + low_temp_today+'\n' + type_today
    print(weather_str)