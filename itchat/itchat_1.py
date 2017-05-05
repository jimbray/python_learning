#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/4/10
__author__ = 'jimbray'

import itchat
import requests
import json

# 处理文本信息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # 微信里，每个用户和群聊，都使用很长的ID来区分
    # msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    reply_text = '"' + msg['Text'] + '"?' + "你这是什么意思?"
    return reply_text


@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text'])
    # 加完好友后，给好友打个招呼
    itchat.send_msg('很高兴认识你', msg['RecommendInfo']['UserName'])


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply_in_group(msg):
    if msg['isAt']:

        print(msg['Text'])
        if '天气' in msg['Text']:
            reply_msg = get_weather_in_shenzhen()
            itchat.send(reply_msg, msg['FromUserName'])
        else:
            itchat.send('嗯，我收到了你的信息, 然后呢', msg['FromUserName'])


def get_weather_in_shenzhen():
    url = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101280601'
    jsonstr = requests.get(url).text

    data = json.loads(jsonstr)
    weather = data['data']

    city = weather['city']
    ganmao = weather['ganmao']
    wendu = weather['wendu'] + '摄氏度'
    forecast = weather['forecast']

    today = forecast[0]

    fengli_today = today['fengli']
    fengxiang_today = today['fengxiang']
    high_temp_today = today['high']
    low_temp_today = today['low']
    type_today = today['type']

    weather_str = city + '\n' + ganmao + '\n' + wendu + '\n' + fengli_today + '\n' + fengxiang_today + '\n' + high_temp_today + '\n' + low_temp_today + '\n' + type_today
    return weather_str


if __name__ == '__main__':
    # 在auto_login()里面提供一个True，即hotReload=True
    # 即可保留登陆状态
    # 即使程序关闭，一定时间内重新开启也可以不用重新扫码

    itchat.auto_login(True)

    # itchat.send('Hello FileHelper', toUserName='filehelper')

    itchat.run()