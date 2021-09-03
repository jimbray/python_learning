#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: api.py 
@time: 2021/08/26
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

import requests

token = 'secret_eDBPm9P3qWEVtx99WI4KYUV8htjp2w9A2b3HIs60kQ5'
database_id = "afed2160dd3c4c45ba1cfcd9c8f28390"
headers = {
    'Authorization': 'Bearer ' + token,
    'Notion-Version': '2021-08-16',
    'Content-Type': 'application/json'
}


def queryDatabase():
    url = 'https://api.notion.com/v1/databases/' + database_id + '/query'

    response = requests.post(url, headers=headers)
    print(response.json())


def addDaily():
    url = 'https://api.notion.com/v1/databases/' + database_id
    data = {
        'properties': '{"key": "value"}'
    }

    response = requests.patch(url, data, headers=headers)
    print(response.json())


def getPageText():
    page_id = '9a184abacb974033813ff696747d13a3'
    url = 'https://api.notion.com/v1/pages/' + page_id
    response = requests.get(url, headers=headers)
    print(response.text)


def addDailyPage():
    url = 'https://api.notion.com/v1/pages'
    data = {
        "parent": {
            "database_id": database_id
        },
        "properties": {
            "Name": {
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": "每日打卡",
                            "link": None
                        },
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default"
                        },
                        "plain_text": "每日打卡",
                        "href": None
                    }
                ]
            }
        },
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.json())


if __name__ == '__main__':
    # queryDatabase()
    # getPageText()
    # addDaily()
    addDailyPage()
# 'properties': {
#             '香信打卡': {
#                 'id': '%3CvCS',
#                 'type': 'checkbox',
#                 'checkbox': True
#             },
#             'Gmail邮件': {
#                 'id': 'RdlZ',
#                 'type': 'checkbox',
#                 'checkbox': True
#             },
#             '日期': {
#                 'id': 'VgTg',
#                 'type': 'formula',
#                 'formula': {
#                     'type': 'string',
#                     'string': '日期：2021-08-26'
#                 }
#             },
#             '微信读书': {
#                 'id': 'WrWu',
#                 'type': 'checkbox',
#                 'checkbox': True
#             },
#             '完成度': {
#                 'id': 'bqQ%3F',
#                 'type': 'formula',
#                 'formula': {
#                     'type': 'string',
#                     'string': '80%'
#                 }
#             },
#             'Created': {
#                 'id': 'hic%3D',
#                 'type': 'created_time',
#                 'created_time': '2021-08-26T07: 42: 00.000Z'
#             },
#             '幼儿园体温接龙': {
#                 'id': 'sK%3Ee',
#                 'type': 'checkbox',
#                 'checkbox': True
#             },
#             '软考读书': {
#                 'id': '%7BMmD',
#                 'type': 'checkbox',
#                 'checkbox': False
#             },
#             'Name': {
#                 'id': 'title',
#                 'type': 'title',
#                 'title': [
#                     {
#                         'type': 'text',
#                         'text': {
#                             'content': '每日打卡',
#                             'link': None
#                         },
#                         'annotations': {
#                             'bold': False,
#                             'italic': False,
#                             'strikethrough': False,
#                             'underline': False,
#                             'code': False,
#                             'color': 'default'
#                         },
#                         'plain_text': '每日打卡',
#                         'href': None
#                     }
#                 ]
#             }
#         }
