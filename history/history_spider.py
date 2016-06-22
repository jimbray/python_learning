# -*- coding : utf-8 -*-
__author__ = 'jimbray'

from flask import Flask
import time
from Scheduler import Scheduler
import json
from data_spider import *
from database_provider import *

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello . I am running.'


@app.route('/1')
def get_history_from_data():
    get_history()
    return 'Done.'


@app.route('/2')
def get_carousel_from_data():
    get_carousel()
    return 'Done.'


def check_time_for_get():
    cur_time = time.ctime()[11:19]
    if cur_time == '00:30:00':
        get_history()
        get_carousel()


@app.route('/today')
def today():
    result = get_all_history_today()
    # return 'This page should be a html.'
    return json.dumps(result, ensure_ascii=False)

@app.route('/api/v0.1/today', methods=['POST'])
def get_today():
    result = get_all_history_today()
    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    scheduler = Scheduler(1, check_time_for_get)
    scheduler.start()

    # app.run(host='0.0.0.0', debug=False, port=1470)
    app.run(debug=True)