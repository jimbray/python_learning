#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/5/17
__author__ = 'jimbray'

import xml.etree.ElementTree as ET


def remove_duplicate():
    string_tree = ET.ElementTree(file='duplicate_strings.xml')
    root = string_tree.getroot()

    all_string_list = []

    for child_of_root in root:
        string_content = str(child_of_root.text)
        all_string_list.append(string_content)

    with open('remove_duplicate_string_result.txt', 'w', encoding='utf-8') as result_file:
        already_added_list = []
        result_content = ''
        for child_of_root in root:
            lower_text = str(child_of_root.text)
            lower_key = str(child_of_root.attrib['name'])
            if lower_text not in already_added_list:
                if lower_text in all_string_list:
                    result_content += '"%s" = "%s"\n' % (lower_key, lower_text)
                    already_added_list.append(lower_text)
        result_file.seek(0)
        result_file.truncate()
        result_file.write(result_content)
    print('Every things is done.')


if __name__ == '__main__':
    remove_duplicate()