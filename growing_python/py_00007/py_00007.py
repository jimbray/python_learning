#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/1/23
__author__ = 'jimbray'

import os
import linecache
import sys

total_count = 0

def cal_code_line(root_dir):
    list = os.listdir(root_dir)

    with open('./result.txt', 'a+', encoding='utf-8') as f:
        for line in list:
            file_path = os.path.join(root_dir, line)
            if os.path.isdir(file_path):
                print('dir -> ' + file_path)
                cal_code_line(file_path)
            elif file_path.endswith('.java'):
                file_line_count = get_java_file_line_count(file_path)
                global total_count
                total_count += file_line_count
                print('file -> ' + file_path + ' and line count is -> ' + str(file_line_count))
                f.write('File(' + file_path + ') has line count is -> ' + str(file_line_count) + '\n')

def get_java_file_line_count(file_path):
    return len(linecache.getlines(file_path))

if __name__ == '__main__':

    root = ''
    if len(sys.argv) > 1:
        print('There is some argv')
        root = sys.argv[1]
    else:
        root = './'
    cal_code_line(root)

    with open('./result.txt', 'a+', encoding='utf-8') as f:
        print('\n')
        print('finally.The total line count is -> ' + str(total_count))
        f.write('\n\n\n')
        f.write('finally.The total line count is -> ' + str(total_count) + '\n\n')
