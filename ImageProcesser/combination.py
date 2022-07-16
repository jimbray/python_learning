#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: combination.py 
@time: 2022/04/25
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

from PIL import Image
import os

IMAGES_FORMAT = ['.jpg', '.png', '.jpeg']


def image_combination():
    imgs_folder = 'E:\\wallpapers'
    imgs_list = os.listdir(imgs_folder)
    single_image_size = 256
    result_row = 12
    result_col = 1

    # 获取所有图片的名称
    image_names = [name for name in os.listdir(imgs_folder) for item in IMAGES_FORMAT if
                   os.path.splitext(name)[1] == item]

    if len(image_names) != result_row * result_col:
        print('图片数量不符合要求')
        return

    result_image = Image.new('RGB', (single_image_size * result_col, single_image_size * result_row))
    # 将图片按照行列排列
    for i in range(result_row):
        for j in range(result_col):
            img_name = image_names[i * result_col + j]
            img = Image.open(os.path.join(imgs_folder, img_name))
            img = img.resize((single_image_size, single_image_size))
            result_image.paste(img, (j * single_image_size, i * single_image_size))

    result_image.save('result.jpg')


if __name__ == '__main__':
    image_combination()
