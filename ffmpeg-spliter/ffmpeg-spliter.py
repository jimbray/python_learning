#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: ffmpeg-spliter.py 
@time: 2022/04/20
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

# 读取两个参数：输入的文件名，开始时间，截取时长
# 输出为输入文件名的前缀+"split"
import os


def split_video(input_file, start_time, duration):
    # 分割视频
    # cmd = "ffmpeg -i {0} -ss {1} -t {2} -c copy {0}_split".format(input_file, start_time, duration)
    cmd = "ffmpeg.exe -ss {1} -t {2} -i {0}  -c:v libx264 -c:a aac -strict " \
          "experimental -b:a 98k {0}_split.mp4".format(input_file, start_time, duration)
    print(cmd)
    # 执行命令
    os.system(cmd)


# 需要先把 ffmpeg 的实际路径 设置为环境变量
if __name__ == '__main__':
    split_video("E:\\BaiduNetdiskDownload\\IDM-Download\\少林足球_2022-04-19_15-53-58.mp4", "00:10:00", 10)