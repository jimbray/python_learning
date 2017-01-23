#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/1/23
__author__ = 'jimbray'

import random

from PIL import Image, ImageDraw, ImageFont

origim_image = './image/yitachi.jpg'
target_image = './image/target_yitachi.jpg'

color = (255, 0, 0)

def get_random_num():
    return random.randint(0, 100)


def draw_text_on_image(origin_image_path, text='no', fill_color=color):
    try:
        image = Image.open(origim_image)
        size = image.size
        x = size[0] - 38
        font = ImageFont.truetype('arial.ttf', 36)
        draw = ImageDraw.Draw(image)
        draw.text((x, 15), text, font=font, fill=fill_color)
        image.save(target_image, 'jpeg')
    except:
        print('Unable to load image')


if __name__ == '__main__':
    draw_text_on_image(origim_image, str(get_random_num()))