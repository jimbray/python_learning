#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:jimbray 
@file: books.py 
@time: 2021/09/03
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

from requests_html import HTMLSession
import csv


def getAllBooksTags():
    tag_list = []
    url = 'https://book.douban.com/tag/'
    session = HTMLSession()
    res = session.get(url)
    # print(res.text)
    tagColList = res.html.find('.tagCol')
    for tagCol in tagColList:
        tdList = tagCol.find('td')
        for td in tdList:
            aList = td.find('a')
            for a in aList:
                tag_list.append(a.text)

    return tag_list


def writeTagsToCsv(tag_list):
    path = 'book_tags.csv'
    with open(path, 'w', newline='', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        head_row = ['标签']
        csv_write.writerow(head_row)
        for tag in tag_list:
            csv_write.writerow([tag])


if __name__ == '__main__':
    tag_list = getAllBooksTags()
    writeTagsToCsv(tag_list)