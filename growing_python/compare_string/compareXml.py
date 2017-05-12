#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/5/12
__author__ = 'jimbray'

import os
import xml.etree.ElementTree as ET

# 查找第一个与指定字符相同的 标签的 name
def find_match_text_key_in_string(text):
    string_tree = ET.ElementTree(file='ios.xml')
    root = string_tree.getroot()
    for child_of_root in root:
        if child_of_root.text == text:
            return str(child_of_root.attrib['name'])
            # print(child_of_root.attrib['name'])
            # print(child_of_root.text)


# def compare():
# with open('different.xml', 'w', encoding='utf-8') as diff_file, open('same.xml', 'w',
#                                                                          encoding='utf-8') as same_file:
#         android_tree = ET.ElementTree(file='android.xml')
#         android_root = android_tree.getroot()
#
#         ios_tree = ET.ElementTree(file='ios.xml')
#         ios_root = ios_tree.getroot()
#
#         same_file_content = ''
#         diff_file_content = ''
#
#         diff_list_line = []
#
#         for child_of_android in android_root:
#             index = 0
#             for child_of_ios in ios_root:
#                 if child_of_android.text == child_of_ios.text:
#                     same_file_content += '<string name="%s">%s</string>\n' % (
#                         child_of_android.attrib['name'], child_of_android.text)
#                     break
#                 # else:
#                 # diff_file_content += '<string name="%s">%s</string>\n' % (
#                 # child_of_android.attrib['name'], child_of_android.text)
#                 # diff_file_content += '<string name="%s">%s</string>\n\n' % (
#                 #     child_of_ios.attrib['name'], child_of_ios.text)
#                 index += 1
#                 # print(str(index) + '<--->' + str(len(ios_root)))
#                 if index == len(ios_root):
#                     diff_file_content += '<string name="%s">%s</string>\n' % (
#                         child_of_android.attrib['name'], child_of_android.text)
#                     diff_file_content += '<string name="%s">%s</string>\n\n' % (
#                         child_of_ios.attrib['name'], child_of_ios.text)
#                 else:
#                     continue
#         diff_file.seek(0)
#         diff_file.truncate()
#         diff_file.write(diff_file_content)
#         same_file.seek(0)
#         same_file.truncate()
#         same_file.write(same_file_content)
#
#         print('Everything is done')


def compare_string():
    with open('Localizable.strings', 'r+', encoding='utf-8') as ios_file, open('same.xml', 'w', encoding='utf-8') as same_file, open(
            'diff.xml', 'w', encoding='utf-8') as diff_file:
        ios_lines = ios_file.readlines()

        for ios_line in ios_lines:
            ios_line_str = ios_line.split('=')
            print(ios_line)


if __name__ == '__main__':
    compare_string()