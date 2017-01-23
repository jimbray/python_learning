#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/1/23
__author__ = 'jimbray'

import json
import xlwt as exw

def get_jaon_from_json():
    word = []
    with open('numbers.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            word.append(line.strip())

    return ''.join(word)


def write_to_xls(json_str):
    print(json_str)
    xls = exw.Workbook()
    numbers = xls.add_sheet('numbers')

    json_data = json.loads(json_str)

    for row in range(len(json_data)):
        for column in range(len(json_data[row])):
            numbers.write(row, column, json_data[row][column])
    xls.save('numbers.xls')

if __name__ == '__main__':
    write_to_xls(get_jaon_from_json())