# -*- coding:utf-8 -*8

__author__ = 'jimbray'


def is_in_words(input):
    word_list = []
    with open('filtered_words.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()
            word_list.append(line)
        if input in word_list:
            print('Freedom')
        else:
            print('Human Rights')

if __name__ == '__main__':
    while True:
        x = input('>> Input : ')
        is_in_words(x)
