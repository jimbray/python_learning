#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/5/5
__author__ = 'jimbray'

import os
import xml.etree.ElementTree as ET

# 获取当前文件夹内所有layout文件列表
def get_all_layout_xml(path):
    file_list = []
    for file_name in os.listdir(path):
        if '.xml' in file_name and 'strings.xml' not in file_name:
            print(file_name)
            file_list.append(file_name)
    return file_list


# 查找第一个与指定字符相同的 标签的 name
def find_match_text_key_in_string(text):
    string_tree = ET.ElementTree(file='string_file/strings.xml')
    root = string_tree.getroot()
    for child_of_root in root:
        if child_of_root.text == text:
            return str(child_of_root.attrib['name'])
            # print(child_of_root.attrib['name'])
            # print(child_of_root.text)


def do_work():
    layout_file_list = get_all_layout_xml('layout_files')
    with open('result.md', 'w', encoding='utf-8') as result_file, open('lost.xml', 'w', encoding='utf-8') as xml_file:
        lost_content_dict = {}
        lost_key_name_list = []
        result_content = ''
        xml_content = ''
        for file in layout_file_list:
            result_content += '### ' + file + '\n'
            with open('layout_files/' + file, 'r+', encoding='utf-8') as file_layout:
                lines = file_layout.readlines()

                rewrite_file_content = ''

                for line in lines:
                    if line != '' and '<!--' not in line:
                        if 'android:text=' in line:
                            if '@string/' not in line:
                                print(line, )
                                text = line[line.index('"') + 1: line.find('"', line.index('"') + 1)]
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

                                    target_key_name = ''.join(text.lstrip().rstrip()
                                                              .replace(' ', '_')
                                                              .replace('"', '')
                                                              .replace("'", '')
                                                              .replace('’', '')
                                                              .replace('!', '')
                                                              .replace('\\', '')
                                                              .replace('/', '_')
                                                              .replace('.', '')
                                                              .replace('(', '_')
                                                              .replace(')', '_')
                                                              .replace(',', '_')
                                                              .replace('?', '')
                                                              .lower().split())

                                    # 如果key name 已经存在
                                    if target_key_name in lost_key_name_list:
                                        lost_content_dict[target_key_name] += 1  # 进行统计
                                        continue
                                    else:
                                        lost_key_name_list.append(target_key_name)
                                        lost_content_dict[target_key_name] = 1
                                        xml_content += '%s%s%s%s%s' % (
                                            '<string name="',
                                            target_key_name,
                                            '">',
                                            text,
                                            '</string>\n')

                                        # file.write(replace_text)
                                        # file.flush()
                        rewrite_file_content += line

                file_layout.seek(0)
                file_layout.truncate()
                file_layout.write(rewrite_file_content)
                result_content += '\n\n'
            result_content += '\n-----------------------------\n'

        for key, value in lost_content_dict.items():
                    if int(value) > 1:
                        # print('%s%s%s%s' % (key, ' 出现了 ', value, ' 次\n'))
                        result_content += '%s%s%s%s' % (key, ' 出现了 ', value, ' 次\n')

        result_file.seek(0)
        result_file.truncate()
        result_file.write(result_content)

        # print(lost_content_dict)

        xml_file.seek(0)
        xml_file.truncate()
        xml_file.write(xml_content)


if __name__ == '__main__':
    do_work()
    # get_all_layout_xml('layout_files')
    # test_str = '     abcd"\\'
    # print(test_str)
    # print(''.join(test_str.split()))
    # print('done')