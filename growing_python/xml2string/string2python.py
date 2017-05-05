#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/5/5
__author__ = 'jimbray'

import os
import xml.etree.ElementTree as ET

# 获取当前文件夹内所有layout文件列表
def get_all_layout_xml():
    file_list = []
    for file_name in os.listdir():
        if '.xml' in file_name and 'strings.xml' not in file_name:
            print(file_name)
            file_list.append(file_name)
    return file_list


def find_match_text_key_in_string(text):
    string_tree = ET.ElementTree(file='strings.xml')
    root = string_tree.getroot()
    for child_of_root in root:
        if child_of_root.text == text:
            return str(child_of_root.attrib['name'])
            # print(child_of_root.attrib['name'])
            # print(child_of_root.text)


def testET():
    string_tree = ET.ElementTree(file='strings.xml')
    root = string_tree.getroot()
    for child_of_root in root:
        # print(child_of_root.attrib['name'])
        print(child_of_root.text)


if __name__ == '__main__':
    layout_file_list = get_all_layout_xml()
    for layout_file in layout_file_list:
        with open(layout_file, 'r+', encoding='utf-8') as file:
            lines = file.readlines()

            rewrite_file_content = ''

            for line in lines:
                if line != '':
                    if 'android:text=' in line:
                        if '@string/' not in line:
                            print(line, )
                            line_num = file.fileno()
                            # print(line[line.index('"') + 1: len(line)-2])
                            text = line[line.index('"') + 1: len(line) - 2]
                            matched_key_name = find_match_text_key_in_string(text)
                            if matched_key_name is not None:
                                replace_text = '%s%s%s%s' % (
                                    line[0: line.index('=')+1], '"@string/', str(matched_key_name), '"\n')
                                print(replace_text)

                                line = line.replace(line, replace_text)
                            else:
                                print("can't find the match text --> ", text)

                                # file.write(replace_text)
                                # file.flush()
                    rewrite_file_content += line
            file.seek(0)
            file.truncate()
            file.write(rewrite_file_content)