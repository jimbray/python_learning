# -*- coding=utf-8 -*-

__author__ = 'jimbray'

import os
import sys


def play_with_vlc(url):
    # os.system('C:\n')
    # os.system('cd \\\n')
    # os.system('cd C:\\Program Files (x86)\\VideoLAN\\VLC\n')
    os.chdir('C:\\Program Files (x86)\\VideoLAN\\VLC')
    os.system('you-get -p vlc.exe ' + url)

if __name__=='__main__':
    # 第一个参数 是 文件路径
    if len(sys.argv) > 1:
        # 至少有一个参数
        url = sys.argv[1]
    else:
        print('请在后面加入播放地址')

    if url is not None:
        play_with_vlc(url)
