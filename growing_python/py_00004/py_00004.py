# -*- coding=utf-8 -*-
__author__ = 'jimbray'

import string

def get_word_count():
    result = {}
    with open('english_article.txt', 'r', encoding='utf-8') as file:

        for line in file.readlines():
            line = ''.join(ch for ch in line if ch not in string.punctuation)
            words = line.split(' ')
            for word in words:
                word = word.strip()
                if word in result.keys():
                    result[word] += 1
                else:
                    result[word] = 1

    for k, v in result.items():
        print(k, "->", v)


if __name__ == '__main__':
    get_word_count()


