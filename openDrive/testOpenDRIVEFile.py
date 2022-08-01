#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:jimbray 
@file: testOpenDRIVEFile.py 
@time: 2019/04/27
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

# A=C/R弧度=(C/R)*(180/π)度
# A为弧度 C 为弧长 R为半径

# 若弧长为l 半径为r
# 则圆心角的弧度数α=l/r

# 弧长l=nπr/180 ∴圆心角n=180l/πr

import math


# def part1():
#     print("----part1------")
#     global lane_width
#     hdg_start = 0
#     length = 20
#     radius = 20
#
#     angle = (180*length)/(math.pi*radius)
#     hdg_end = math.pi / (180.00 / angle)
#     curvature = 1 / radius
#
#     x = 0
#     y = 0
#
#     print("弧度:" + str(hdg_start))
#     print("弧长:" + str(length))
#     print("曲率:" + str(curvature))
#     print("半径:" + str(radius))
#     print("x:" + str(x))
#     print("y:" + str(y))
#
#     print("----part1------")
#     result = [radius, hdg_end]
#     return result
#
#
# def part2(pre_part):
#     print("----part2------")
#     global lane_width
#     hdg_start = pre_part[1]
#     length = 20
#     radius = 20
#
#     angle = (180*length)/(math.pi*radius)
#     hdg_end = math.pi / (180.00 / angle)
#     curvature = 1 / radius
#
#     x = pre_part[0] * math.sin(pre_part[1])
#     y = radius - radius * math.cos(hdg_end)
#
#     print("弧度:" + str(hdg_start))
#     print("弧长:" + str(length))
#     print("曲率:" + str(curvature))
#     print("半径:" + str(radius))
#     print("x:" + str(x))
#     print("y:" + str(y))
#
#     print("----part2------")
#     result = [radius, hdg_end]
#     return result
#
#
# def part3(pre_part):
#     print("----part3------")
#     global lane_width
#
#     hdg_start = pre_part[1]
#     length = 20
#     radius = 20
#
#     hdg_end = (length / radius) * (180 / math.pi)
#     curvature = 1 / radius
#
#     x = pre_part[0] * math.sin(pre_part[1])
#     y = radius - radius * math.cos(hdg_end)
#
#     print("弧度:" + str(hdg_end))
#     print("弧长:" + str(length))
#     print("曲率:" + str(curvature))
#     print("半径:" + str(radius))
#     print("x:" + str(x))
#     print("y:" + str(y))
#
#     print("----part3-----")
#     result = [radius, hdg_end]
#     return result
#
#
# def cal():
#     part3(part2(part1()))


lane_width = 1


def calPart(part_num, pre_radius, pre_hdg_end):
    global lane_width
    print('---------part%d----------' % part_num)
    hdg_start = 0 if part_num == 0 else pre_hdg_end

    length = 20
    if part_num == 0 or part_num == 1:
        length = 20
    elif part_num == 3:
        length = 60

    radius = 20
    if part_num == 0 or part_num == 1:
        radius = 20
    elif part_num == 3:
        radius = 60

    angle = (180 * length) / (math.pi * radius)
    hdg_end = 0 if part_num == 0 else math.pi / (180.00 / angle)
    curvature = 1 / radius

    x = pre_radius * math.sin(pre_hdg_end)
    y = radius - radius * math.cos(pre_hdg_end)

    print("弧度:" + str(hdg_start))
    print("弧长:" + str(length))
    print("曲率:" + str(curvature))
    print("半径:" + str(radius))
    print("x:" + str(x))
    print("y:" + str(y))

    print('---------part%d----------' % part_num)

    part_num = part_num + 1
    if part_num <= 3:
        calPart(++part_num, radius, hdg_end)


def startCal():
    global lane_width
    part = 1
    original_raduis = 20 * lane_width
    original_hdg_start = 0
    calPart(part, original_raduis, original_hdg_start)


if __name__ == '__main__':
    startCal()
    # part3(part2(part1()))
