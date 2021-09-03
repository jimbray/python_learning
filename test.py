# -*- coding: utf-8 -*-

__author__ = 'jimbray'
import math

# import os,datetime
#
# def get_release_time():
#     today = datetime.datetime.now()
#     return today.strftime('%Y-%m-%d-%H-%M-%S')
#
# def copy_apk_to_release_share_folder():
#     dir_name = 'C:\\Users\\dell\\.jenkins\\workspace\\Poof-Android\\app\\build\\outputs\\apk\\'
#     target_dir_name = 'H:\\Poof_for_Android_Release\\'
#     for file in os.listdir(dir_name):
#         source_file_full_name = os.path.join(dir_name, file)
#         target_file_full_name = os.path.join(target_dir_name, file)
#         target_file_full_name = target_file_full_name.replace('Poof-', 'Poof-' + get_release_time() + '-')
#         if os.path.isfile(source_file_full_name):
#             os.system('copy %s %s' % (source_file_full_name, target_file_full_name))


def part1():
    print("----part1------")
    global lane_width
    hdg_start = 0
    radius = 20 * lane_width
    hdg_end = math.pi / 3
    length = hdg_end * radius
    curvature = 1 / radius
    x = 0
    y = 0

    print("弧度:" + str(hdg_start))
    print("弧长:" + str(length))
    print("曲率:" + str(curvature))
    print("半径:" + str(radius))
    print("x:" + str(x))
    print("y:" + str(y))

    print("----part1------")
    result = [radius, hdg_end]
    return result


def part2(pre_part):
    print("----part2------")
    global lane_width
    hdg_start = pre_part[1]
    radius = 20 * lane_width
    hdg_end = pre_part[1] - radius * math.sin(math.pi / 3)
    length = pre_part[1] * radius
    curvature = 1 / radius
    x = pre_part[0] * math.sin(pre_part[1])
    y = radius - radius * math.cos(math.pi / 3)

    print("弧度:" + str(hdg_start))
    print("弧长:" + str(length))
    print("曲率:" + str(curvature))
    print("半径:" + str(radius))
    print("x:" + str(x))
    print("y:" + str(y))

    print("----part2------")
    result = [radius, hdg_end]
    return result


def part3(pre_part):
    print("----part3------")
    global lane_width
    hdg_start = 0
    radius = 20 * lane_width
    hdg_end = math.pi / 3
    length = hdg_end * radius
    curvature = 1 / radius
    x = pre_part[0] * math.sin(pre_part[1])
    y = radius - radius * math.cos(math.pi / 3)

    print("弧度:" + str(hdg_start))
    print("弧长:" + str(length))
    print("曲率:" + str(curvature))
    print("半径:" + str(radius))
    print("x:" + str(x))
    print("y:" + str(y))

    print("----part3-----")
    result = [radius, hdg_end]
    return result


def cal():
    part3(part2(part1()))


lane_width = 1


def calPart(part_num, pre_radius, pre_hdg_end, pre_length):
    global lane_width
    print('---------part%d----------' % part_num)
    gdh_start = pre_hdg_end
    radius = 20 * lane_width
    hdg_end = pre_hdg_end - radius * math.sin(math.pi / 3)
    length = pre_length

    curvature = 1 / radius
    if part_num == 1:
        x = 0
        y = 0
    else :
        x = pre_radius * math.sin(pre_hdg_end)
        y = radius - radius * math.cos(math.pi / 3)

    print("弧度:" + str(pre_hdg_end))
    print("弧长:" + str(length))
    print("曲率:" + str(curvature))
    print("半径:" + str(radius))
    print("x:" + str(x))
    print("y:" + str(y))

    print('---------part%d----------' % part_num)

    part_num = part_num + 1
    if part_num <= 5:
        calPart(++part_num, radius, hdg_end, length)


def startCal():
    global lane_width
    part = 1
    original_raduis = 20 * lane_width
    original_hdg_start = 0
    original_length = 20
    calPart(part, original_raduis, original_hdg_start, original_length)


if __name__ == '__main__':
    # copy_apk_to_release_share_folder()
    # startCal()
    part3(part2(part1()))
