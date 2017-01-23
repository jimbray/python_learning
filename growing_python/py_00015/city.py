#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/1/23
__author__ = 'jimbray'

import json
import xlwt as exw

def get_json_from_file():
    word = []
    with open('city.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            word.append(line.strip())
    return ''.join(word)


def write_to_xls(json_str):
    print(json_str)
    json_data = json.loads(json_str)

    xls = exw.Workbook()
    city = xls.add_sheet('city')

    for row in range(len(json_data)):
        for column in range(2):
            if column == 0:
                city.write(row, 0, str(row+1))
            else:
                city.write(row, column, json_data[str(row + 1)])
    xls.save('city.xls')

if __name__ == '__main__':
    write_to_xls(get_json_from_file())