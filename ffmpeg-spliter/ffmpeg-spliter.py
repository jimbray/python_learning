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
import argparse


# get params from command line
def get_params():
    parser = argparse.ArgumentParser()
    # parser.add_argument('-i', '--input', help='input file path', required=True)
    # parser.add_argument('-s', '--start', help='start time', required=True)
    # parser.add_argument('-d', '--duration', help='duration', required=True)

    parser.add_argument('input', help='input file path')
    parser.add_argument('start', help='start time')
    parser.add_argument('-d', '--duration', help='duration')
    parser.add_argument('-e', '--end', help='end time')
    args = parser.parse_args()
    return args


# 计算两个时间的差值，以秒为单位
def get_time_diff(start, end):
    start_hour, start_min, start_sec = start.split(":")
    end_hour, end_min, end_sec = end.split(":")
    start_time = int(start_hour) * 3600 + int(start_min) * 60 + int(start_sec)
    end_time = int(end_hour) * 3600 + int(end_min) * 60 + int(end_sec)
    return end_time - start_time


# 通过时长参数分割视频
def split_video_by_duration(input_file_path, start_time, duration):
    # 分割视频
    # 获取input_file 的前缀
    input_file_prefix = input_file_path.split(".")[0]
    start_time_str = start_time.replace(":", "-")
    cmd = "ffmpeg.exe -ss {2} -t {3} -i {0}  -c:v libx264 -c:a aac -strict " \
          "experimental -b:a 98k {1}_{4}_{3}.mp4".format(input_file_path, input_file_prefix, start_time, duration, start_time_str)
    # print(cmd)
    # 执行命令
    os.system(cmd)


# 通过结束时间参数分割视频
def split_video_by_endtime(input_file_path, start_time, end_time):
    # 分割视频
    input_file_prefix = input_file_path.split(".")[0]
    start_time_str = start_time.replace(":", "-")
    end_time_str = end_time.replace(":", "-")
    cmd = "ffmpeg.exe -ss {2} -t {3} -i {0}  -c:v libx264 -c:a aac -strict " \
          "experimental -b:a 98k {1}_{4}_{5}.mp4".format(input_file_path, input_file_prefix, start_time, get_time_diff(start_time, end_time), start_time_str, end_time_str)
    # print(cmd)
    # 执行命令
    os.system(cmd)


# 需要先把 ffmpeg 的实际路径 设置为环境变量
if __name__ == '__main__':
    args = get_params()
    input_file = args.input
    start_time = args.start
    duration = args.duration
    end_time = args.end
    if duration is None and end_time is None:
        print("duration or end_time is required")
        exit(1)

    if duration is not None:
        split_video_by_duration(input_file, start_time, duration)
    else:
        split_video_by_endtime(input_file, start_time, end_time)