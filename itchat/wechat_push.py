#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: wechat_push.py 
@time: 2021/04/02
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""
import requests


def sendMessage(token, text) :
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token

    toUser = "@all"
    msgtype = "text"
    agentid = 1000002

    res = requests.post(url, json={"touser": "@all", "msgtype": "text", "agentid": 1000002, "text": {"content": text}})

    print(res.json())


def getToken():
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww07d952bc13032c5e&corpsecret=t6957hae9Ef6eR8u4sgAjHfSSpfavYK52KLWE6CDvyI"
    res = requests.get(token_url)

    token = ''
    if res.status_code == 200:
        print(res.json()['access_token'])
        token = res.json()['access_token']
    return token


if __name__ == '__main__':
    token = getToken()
    if token == '':
        # 没有token
        pass
    else :
        sendMessage(token, "准备推送")
# var
# msg = require("./wechat_message_obj");
#
# var
# token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww07d952bc13032c5e&corpsecret=t6957hae9Ef6eR8u4sgAjHfSSpfavYK52KLWE6CDvyI"
# var
# res = http.get(token_url)
#
# var
# token;
#
# if (res.statusCode == 200) {
# var access = res.body.json();
# log(access)
#
# token = access.access_token;
#
# message_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token
#
# // var agentid = 1000002;
#
# log(message_url);
#
# var txt = msg.msg;
# var res_msg = http.postJson(message_url, {
# "touser": "@all",
#           "msgtype": "text",
# "agentid": 1000002,
# "text": {
#     "content": txt
# }
# });
#
# log(res_msg.body.json());
# }
