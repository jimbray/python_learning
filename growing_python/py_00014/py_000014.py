# -*- coding=utf-8 -*-
__author__ = 'jimbray'

import json
import xlwt as ew

def get_file_json():
    word_list = []
    with open('students.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            word_list.append(line.strip())
    return ''.join(word_list)


def write_to_excel(json_str):
    print(json_str)
    xls = ew.Workbook()
    sheet = xls.add_sheet('students')
    json_data = json.loads(json_str)

    for row in range(len(json_data)):
        for column in range(len(json_data[str(row + 1)]) + 1):
            if column == 0:
                sheet.write(row, column, str(row+1))
            else:
                sheet.write(row, column, json_data[str(row + 1)][column - 1])

    xls.save('students.xls')

if __name__ == '__main__':
    write_to_excel(get_file_json())

