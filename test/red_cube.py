#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: red_cube.py 
@time: 2021/11/26
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""
import time

import hashlib
import urllib3
import json

import sys

type = sys.getfilesystemencoding()

base_url = "http://webchatapi.sz-redcube.com"
user_agent = "Mozilla/5.0 (Linux; Android 11; KB2000 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/2993 MicroMessenger/8.0.16.2040(0x28001053) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64"
cookies = "Hm_lvt_e67bacebe17684e796477e4caf93afe1=1637908127; Hm_lpvt_e67bacebe17684e796477e4caf93afe1=1637908391"

global_headers = {
    "user-agent": user_agent,
    'Content-Type': 'application/json',
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept": "*/*",
    'Cookie': "Hm_lvt_e67bacebe17684e796477e4caf93afe1=1637908127; Hm_lpvt_e67bacebe17684e796477e4caf93afe1=1637908391",
    "Connection": "keep-alive"
}

sign_key = 'srAO407hOx04NrP1g3rDoIWzaTO4fda7F'
device_id = '59692b62-1814-9ffc-8774-f8a2db4fcce5'


# 预约
def reservation():
    action = "/reservation/activity/doReservationNew"
    url = base_url + action
    print("url: " + url)

    timestamp = get_cur_time_13()

    # 10316 是 11月27
    # 10318 是 12月04

    date_id = "10316"

    global device_id
    data = {
        # 设备id
        "deviceId": device_id,
        # 13位 时间戳
        "sendTime": timestamp,
        # 签名
        "sign": signParam(timestamp),
        # 活动id
        "activityId": "11",
        # 申请的用户名
        "activityModifyUser": "656377",
        # 不知道是什么
        "activityType": 4,
        # 最高预约人数？
        "activityMaxPeople": "150",
        # 日期，不知道怎么得出来的
        "activityDateId": date_id,
        # 四个联系人
        "activityAddressZh": "1495754,1495756,1495757,1495758",
        # 看上去像支付状态，3 应该是已支付吧
        "paymentStatus": 3,
        # 报名活动，好像是固定66
        "baomingActivityType": 66
    }
    post_operation(url, data, timestamp)


# 获取用户详细信息
def user_details():
    action = "/user/user/detail"
    url = base_url + action
    print("url: " + url)

    timestamp = get_cur_time_13()
    data = {
        "deviceId": "59692b62-1814-9ffc-8774-f8a2db4fcce5",
        "sendTime": timestamp,
        "sign": signParam(timestamp),
        "userId": "656377"
    }

    post_operation(url, data, timestamp)


# 获取用户信息
def get_sys_user():
    action = "/user/user/getSysUser"
    url = base_url + action
    print("url: " + url)

    timestamp = get_cur_time_13()
    data = {
        "deviceId": "59692b62-1814-9ffc-8774-f8a2db4fcce5",
        "sendTime": timestamp,
        "sign": signParam(timestamp),
        "userId": "656377"
    }

    post_operation(url, data, timestamp)


# 获取联系人信息
def get_contact_list():
    action = "/user/contact/contactList"
    url = base_url + action
    print("url: " + url)
    timestamp = get_cur_time_13()

    data = {
        "deviceId": "59692b62-1814-9ffc-8774-f8a2db4fcce5",
        "sendTime": timestamp,
        "sign": signParam(timestamp),
        "userId": "656377",
        "accessToken": "?", # accesstoken 怎么获取？
        "pageNumb": 1
    }


def user_page():
    action = "/other/weixinNew/userPage/2"
    url = base_url + action

    get_operation(url)


# 实际post操作
def post_operation(url, data, timestamp):
    body_data = json.dumps(data).encode('utf-8')

    global global_headers
    http = urllib3.PoolManager()
    response = http.request("POST", url=url, headers=global_headers, body=body_data)

    print(str(response.data, encoding='utf-8'))


def get_operation(url):
    http = urllib3.PoolManager()
    response = http.request("GET", url=url)
    print(str(response, encoding='utf-8'))


# device_id 就是前面的device_id,如果没有，也可以生成，代码里面是 guid()函数
# sendTime 是发送时间 13位的
# 关键签名就是这三者加起来的 md5 加密，js里面是hex_md5,Python里面直接就用 hashlib 的md5,本来不知道行不行，现在确认可以
def signParam(timestamp):
    global device_id
    # timestamp = int(round(time.time() * 1000))
    print("timestamp：" + str(timestamp))

    sign_str = str(device_id + str(timestamp) + sign_key).encode("utf-8")

    n = hashlib.md5()
    n.update(sign_str)
    sign = n.hexdigest()
    print("sign：" + sign.upper())
    return sign.upper()


def get_cur_time_13():
    return int(round(time.time() * 1000))


if __name__ == '__main__':
    # get_sys_user()
    #
    # user_details()
    #
    # user_page()

    reservation()
    # print(int(round(time.time() * 1000)))
    # signParam()




















##################以下是一些记录#########################
# {
# 	"deviceId": "59692b62-1814-9ffc-8774-f8a2db4fcce5",
# 	"sendTime": 1637909428516,
# 	"sign": "133B18F976A322E070A150735FC72688",
# 	"activityId": "132",
# 	"activityModifyUser": "656377",
# 	"activityType": 4,
# 	"activityMaxPeople": "1712",
# 	"activityDateId": "10314",
# 	"activityAddressZh": "1495754,1495756,1495757,1495758",
# 	"paymentStatus": 3,
# 	"baomingActivityType": 66
# }

# GET /other/weixin/getWxAccessTokenUserPage?code=041xu7ml2w1nc84Kbanl2YDsWp2xu7mC&state=1 HTTP/1.1
# user-agent:Mozilla/5.0 (Linux; Android 11; KB2000 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/2993 MicroMessenger/8.0.16.2040(0x28001053) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64
# cookie: Hm_lvt_e67bacebe17684e796477e4caf93afe1=1637908127; Hm_lpvt_e67bacebe17684e796477e4caf93afe1=1637908391

# /**
#  * 组一般签名
#  * @return {Object} {
#  *          deviceId:设备ID
#  *          sendTime: 时间 13 位
#  *          sign: 签名
#  *         }
#  */
# function signParam() {
#   var cliendId = getClientId();
#   var timestamp = new Date().getTime();
#   var sign = hex_md5(cliendId + timestamp + signKey).toUpperCase()
#   var param = {
#     "deviceId":cliendId,
#     "sendTime":timestamp,
#     "sign":sign
#   }
#   return param;
# }
