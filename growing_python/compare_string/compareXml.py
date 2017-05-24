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



def compare():
    with open('android_different.xml', 'w', encoding='utf-8') as android_diff_file, open('ios_different.xml', 'w',
                                                                                         encoding='utf-8') as ios_diff_file, open(
            'same.xml', 'w', encoding='utf-8') as same_file:
        android_tree = ET.ElementTree(file='android_string.xml')
        android_root = android_tree.getroot()

        ios_tree = ET.ElementTree(file='project_strings.xml')
        ios_root = ios_tree.getroot()

        same_file_content = ''
        android_diff_file_content = ''
        ios_diff_file_content = ''

        diff_list_line = []

        for child_of_android in android_root:
            index = 0
            for child_of_ios in ios_root:
                if child_of_android.text == child_of_ios.text:
                    # same_file_content += '<string name="%s">%s</string>\n' % (
                    #     child_of_android.attrib['name'], child_of_android.text)
                    break
                # else:
                # diff_file_content += '<string name="%s">%s</string>\n' % (
                # child_of_android.attrib['name'], child_of_android.text)
                # diff_file_content += '<string name="%s">%s</string>\n\n' % (
                # child_of_ios.attrib['name'], child_of_ios.text)
                index += 1
                # print(str(index) + '<--->' + str(len(ios_root)))
                if index == len(ios_root):
                    android_diff_file_content += '<string name="%s">%s</string>\n' % (
                        child_of_android.attrib['name'], child_of_android.text)
                    # diff_file_content += '<string name="%s">%s</string>\n\n' % (
                    # child_of_ios.attrib['name'], child_of_ios.text)
                else:
                    continue

        for child_of_ios in ios_root:
            index = 0
            for child_of_android in android_root:
                if child_of_android.text == child_of_ios.text:
                    same_file_content += '<string name="%s">%s</string>\n' % (
                        child_of_android.attrib['name'], child_of_android.text)
                    break
                # else:
                # diff_file_content += '<string name="%s">%s</string>\n' % (
                # child_of_android.attrib['name'], child_of_android.text)
                # diff_file_content += '<string name="%s">%s</string>\n\n' % (
                # child_of_ios.attrib['name'], child_of_ios.text)
                index += 1
                # print(str(index) + '<--->' + str(len(ios_root)))
                if index == len(android_root):
                    # diff_file_content += '<string name="%s">%s</string>\n' % (
                    # child_of_android.attrib['name'], child_of_android.text)
                    ios_diff_file_content += '<string name="%s">%s</string>\n' % (
                        child_of_ios.attrib['name'], child_of_ios.text)
                else:
                    continue
        android_diff_file.seek(0)
        android_diff_file.truncate()
        android_diff_file.write(android_diff_file_content)
        ios_diff_file.seek(0)
        ios_diff_file.truncate()
        ios_diff_file.write(ios_diff_file_content)

        same_file.seek(0)
        same_file.truncate()
        same_file.write(same_file_content)

        print('Everything is done')


# def compare_string():
# with open('iso.txt', 'r+', encoding='utf-8') as ios_file, open('same.xml', 'w', encoding='utf-8') as same_file, open(
# 'diff.xml', 'w', encoding='utf-8') as diff_file:
# ios_lines = ios_file.readlines()
#
# for ios_line in ios_lines:
# ios_line_str = ios_line.split('=')
# print(ios_line)


def convert_txt_to_xml():
    with open('string.txt', 'r', encoding='utf-8') as ori_file, open('android_string.xml', 'w+', encoding='utf-8') as target_file:
        ios_lines = ori_file.readlines()

        target_file_content = '<ios>\n'

        for ios_line in ios_lines:
            ios_line_str_array = ios_line.split('=')
            if len(ios_line_str_array) > 1:

                key = ''.join(ios_line_str_array[0])
                value = ''.join(ios_line_str_array[1])

                # 对 key 和 value 做一下处理
                key = ''.join(key)
                key = key[1:key.find('"', 1)]

                value = value.lstrip()
                value = value[1:value.find('"', 1)]
                value = value.replace('&', 'and')

                print(key + '->' + value)
                content_str = '<string name="%s">%s</string>\n' % (
                    key, value)
                target_file_content += content_str
            else:
                print('array length failed')

        target_file_content += '</ios>'
        target_file.seek(0)
        target_file.truncate()
        target_file.write(target_file_content)


def find_different_between_file():
    with open('lost.xml', 'w', encoding='utf-8') as lost_file, open('same.xml', 'w', encoding='utf-8') as sam_file:
        ori_tree = ET.ElementTree(file='project_strings.xml')
        ori_root = ori_tree.getroot()

        being_compare_tree = ET.ElementTree(file='android_string.xml')
        being_compare_root = being_compare_tree.getroot()

        same_content = ''
        lost_content = ''

        for old_item in ori_root:
            key_name = old_item.attrib['name']
            hasSame = False
            for new_item in being_compare_root:
                if new_item.attrib['name'] == key_name:
                    same_content += '<string name="%s">%s</string>\n' % (key_name, old_item.text)
                    hasSame = True
                    break

            if not hasSame:
                lost_content += '<string name="%s">%s</string>\n' % (key_name, old_item.text)

        lost_file.seek(0)
        lost_file.truncate()
        lost_file.write(lost_content)

        sam_file.seek(0)
        sam_file.truncate()
        sam_file.write(same_content)

if __name__ == '__main__':
    convert_txt_to_xml()
    # compare()
    # find_different_between_file()