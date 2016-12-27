# -*- coding: utf-8 -*-
__author__ = 'jimbray'

def is_in_words(input_str):
    word_list = []
    result_str = str(input_str)
    with open('filtered_words.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()

            if result_str.find(line) > -1:
                result_str = result_str.replace(line, '**')
        print(result_str)

if __name__ == '__main__':
    while True:
        x = input('>> Input : ')
        is_in_words(x)