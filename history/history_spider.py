# -*- coding : utf-8 -*-
__author__ = 'jimbray'

from flask import Flask
import datetime
import urllib2
from bs4 import BeautifulSoup
import json
from database_helper import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello . I am running.'

@app.route('/hello')
def hello_world():
    return 'Hello Flask'

@app.route('/start')
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
            header_img_url = title_a.attrs['rel']
        else:
            header_img_url = ''

        history = History(title, target_url, header_img_url)
        history.save_to_database()
        print('title->%s url->%s img->%s' % (title, target_url, header_img_url))


    return 'Done'


if __name__ == '__main__':
    app.run(debug=True)