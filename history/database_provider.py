# -*- coding : utf-8 -*-
__author__ = 'jimbray'

from database_helper import *
import datetime


def get_all_history_today():
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    return get_history_by_date(month, day)
