# -*- coding:utf-8 -*-
__author__ = 'jimbray'

from PIL import ImageGrab
import time

def save_clipboard_image():
    pic = ImageGrab.grab()
    pic.save("img_" + str(time.time()) + ".jpg")

if __name__ == '__main__':
    save_clipboard_image()