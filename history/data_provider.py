# -*- coding : utf-8 -*-
__author__ = 'jimbray'

import datetime
import urllib2
from bs4 import BeautifulSoup
from database_helper import *


def get_history():
    print('Spider is comming...')
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    print('month -> %d and day-> %d' % (month, day))
    base_url = 'http://www.lssdjt.com/' + str(month) + '/' + str(day)
    request = urllib2.Request(base_url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read(), 'html.parser')

    # soup.prettify()

    # all_li = soup.find_all('li', class_='gong')
    # li_list = []
    # for li in all_li:
    #     title = li.text
    #
    # json_str = json.dumps(li_list, ensure_ascii=False)
    # return json_str
    result_li = soup.find_all('li', class_='gong')
    for li in result_li:
        title_a = li.contents[0]
        title = title_a.text
        target_url = title_a.attrs['href']
        if 'rel' in title_a.attrs:
            header_img_url_arr = title_a.attrs['rel']
        else:
            header_img_url_arr = None

        if header_img_url_arr is not None:
            pass
            if len(header_img_url_arr) > 0:
                header_img_url = header_img_url_arr[0]
            else:
                header_img_url = ''
        else:
            header_img_url = ''

        history = History(title, target_url, header_img_url.encode('utf-8').strip())
        history.save_to_database()
        print('title->%s url->%s img->%s' % (title, target_url, header_img_url))


def get_carousel():
    print('Spider is comming...')
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    print('month -> %d and day-> %d' % (month, day))
    base_url = 'http://www.lssdjt.com/' + str(month) + '/' + str(day)
    request = urllib2.Request(base_url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read(), 'html.parser')

    all_div = soup.find('div', id='slideshow').find_all('div')
    for dd in all_div:
        title = dd.text
        print(title)
        all_a = dd.find_all('a')
        img_url = all_a[0].find('img')['src']
        carousel = Carousel(title.encode('utf-8').strip(), img_url.encode('utf-8').strip())
        carousel.save_to_database()
        print('title->%s img_url->%s' % (title.encode('utf-8').strip(), img_url.encode('utf-8').strip()))
