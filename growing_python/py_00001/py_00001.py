# -*- coding=utf-8 -*-
__author__ = 'jimbray'

import string, random

# 生成 由大写字母与数字 生成的 默认6位数的 随机字符串
# 使用场景：随机优惠码
def str_generator(size=6, chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__=='__main__':
    with open("id_generator.txt", "w", encoding='utf-8') as file:
        for count in range(200):
            result = '优惠码 NO. ' + str(count+1) + str_generator() + "\n"
            file.write(str(result))


