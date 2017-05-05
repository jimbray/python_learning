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


# 查找第一个与指定字符相同的 标签的 name
def find_match_text_key_in_string(text):
    string_tree = ET.ElementTree(file='strings.xml')
    root = string_tree.getroot()
    for child_of_root in root:
        if child_of_root.text == text:
            return str(child_of_root.attrib['name'])
            # print(child_of_root.attrib['name'])
            # print(child_of_root.text)


def do_work():
    layout_file_list = get_all_layout_xml()
    with open('result.md', 'w', encoding='utf-8') as result_file, open('lost.xml', 'w', encoding='utf-8') as xml_file:
        result_content = ''
        xml_content = ''
        for file in layout_file_list:
            result_content += '### ' + file + '\n'
            with open(file, 'r+', encoding='utf-8') as file_layout:
                lines = file_layout.readlines()

                rewrite_file_content = ''

                for line in lines:
                    if line != '':
                        if 'android:text=' in line:
                            if '@string/' not in line:
                                print(line, )
                                text = line[line.index('"') + 1: len(line) - 2]
                                matched_key_name = find_match_text_key_in_string(text)

                                result_content += line.lstrip().rstrip()
                                result_content += '---> '
                                if matched_key_name is not None:


                                    replace_text = '%s%s%s%s' % (
                                        line[0: line.index('=') + 1], '"@string/', str(matched_key_name), '"\n')
                                    print(replace_text)

                                    result_content += replace_text
                                    result_content += '(successful)\n'

                                    line = line.replace(line, replace_text)
                                else:
                                    print("can't find the match text --> ", text)
                                    result_content += '(failed)\n'
                                    xml_content += '%s%s%s%s%s' % (
                                        '<string name="',
                                        text.lstrip().rstrip().replace(' ', '_').replace('"', '').replace("'", ''),
                                        '">', text,
                                        '</string>\n')

                                    # file.write(replace_text)
                                    # file.flush()
                        rewrite_file_content += line
                file_layout.seek(0)
                file_layout.truncate()
                file_layout.write(rewrite_file_content)
                result_content += '\n\n'
            result_content += '\n\n\n'
        result_file.seek(0)
        result_file.truncate()
        result_file.write(result_content)

        xml_file.seek(0)
        xml_file.truncate()
        xml_file.write(xml_content)


if __name__ == '__main__':
    do_work()