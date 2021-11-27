#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:jimbray 
@file: movies.py 
@time: 2021/09/03
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""
from requests_html import HTMLSession
# base_url = 'https://movie.douban.com/tag/#/'
base_url = 'https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=&start=0'


def getAllForm():
    form_list = []
    session = HTMLSession()
    res = session.get(base_url)
    tags = res.html.find('#app')[0]
    print(tags.html)
    # formTags = tags[0]
    # for tag in formTags:
    #     print(tag)
    #     for li in tag.find('li'):
    #         print(li)

    # return tag_list


if __name__=='__main__':
    forms = getAllForm()