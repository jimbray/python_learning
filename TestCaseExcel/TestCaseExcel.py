#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: TestCaseExcel.py 
@time: 2019/03/06
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

import itertools
from multiprocessing import Process
import xlwt

# 无人车速度 speed >= 10 and speed <= 50
vehicle_speed_list = list(range(10, 21, 10))
print(vehicle_speed_list)

# 无人车载重 load_weight >= 50kg and load_weight <= 500kg
vehicle_load_weight_list = [0, 500]
print(vehicle_load_weight_list)

# 无人车行车轨迹
vehicle_driving_track_list = ["前进-直行", "前进-转弯",
                              "前进-减速带", "前进-转弯-减速带",
                              "后退-直行", "后退-转弯",
                              "后退-减速带", "后退-转弯-减速带",
                              "掉头"]
print(vehicle_driving_track_list)

# 道路坡度 road slope 1% - 35% 0 度 与 8度
vehicle_road_slope_list = [0, 8]
print(vehicle_road_slope_list)

# 障碍物类型
# obstacle_type_list = ["静态", "动态"]
obstacle_type_list = ["静态"]
print(obstacle_type_list)

# 障碍物形状
obstacle_shape_list = ["立方体", "圆柱体", "不规则"]
print(obstacle_shape_list)

obstacle_material_list = ["塑料", "石材", "金属", "玻璃"]
print(obstacle_material_list)

# 环境能见度 5m ~ 100m
environment_visibility = list(range(50, 501, 50))
print(environment_visibility)

# 天气
# weather_type_list = ["晴",
#                      "小雨", "中雨", "大雨", "暴雨",
#                      "多云", "阴天",
#                      "小雪", "中雪", "大雪", "暴雪",
#                      "大雾", "沙尘暴", "雾霾"]
weather_type_list = ["晴",
                     "雨天",
                     "阴天",
                     "雾霾"]
print(weather_type_list)

# 昼夜
day_and_night_list = ["白天", "黑夜"]
print(day_and_night_list)

# 风速方向 相对车头中心
wind_direction_list = ["顺风", "逆风"]
print(wind_direction_list)

# 风速
# wind_speed_list = list(range(0, 37, 3))
wind_speed_list = [5, 20]
print(wind_speed_list)

# 是否有超车条件
is_overtake_list = ["有", "无"]
print(is_overtake_list)

# 优先级
priority_level_list = ["紧急", "不紧急"]
print(priority_level_list)

# 重要级
important_level_list = ["重要", "不重要"]
print(important_level_list)

total_list = vehicle_speed_list + vehicle_load_weight_list + \
             vehicle_driving_track_list + vehicle_road_slope_list + \
             obstacle_type_list + obstacle_shape_list + obstacle_material_list + \
             environment_visibility + weather_type_list + day_and_night_list + \
             wind_direction_list + wind_speed_list + is_overtake_list + \
             priority_level_list + important_level_list


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def writeExcel(list):
    xlsx = xlwt.Workbook(encoding='UTF-8', style_compression=2)
    sheet = xlsx.add_sheet("TestCase", True)

    # 分批写入
    # 每次 5k 条
    part = len(list) // 5000
    last_part = len(list) % 5000
    print("part: " + str(part))
    for part_index in range(0, part):
        start = 0
        if part_index > 0:
            start = 1
        print("[" + str((5000*part_index + start)) + "]-[" + str(5000*(part_index+1)) + "]")
        for row in range(5000*part_index + start, 5000*(part_index+1)):
            line = list[row]
            for column in range(0, len(line)):
                sheet.write(row + 2, column + 3, line[column], set_style("style", 220))

    # 还有最后一波
    print("last part : [" + str((5000*part + 1)) + "]-[" + str(5000*part + last_part) + "]")
    sheet.write((5000*part + 1) + 2, (5000*part + last_part) + 3, line[(5000*part + last_part)], set_style("style", 220))
    xlsx.save("TestCase.xls")
    print("文件写入完成")


def cal():
    result = list(itertools.product(vehicle_speed_list, vehicle_load_weight_list,
                                    vehicle_driving_track_list, vehicle_road_slope_list,
                                    obstacle_type_list, obstacle_shape_list, obstacle_material_list,
                                    environment_visibility, weather_type_list, day_and_night_list,
                                    wind_direction_list, wind_speed_list, is_overtake_list))
    print("list size: " + str(len(result)))
    # print(result)
    writeExcel(result)
    # print(list(itertools.permutations(["ABCD", "123"], 2)))
    # print(list(itertools.product(["ABCD", "123"], 2)))


if __name__ == '__main__':
    cal_precess = Process(target=cal)
    cal_precess.start()
    cal_precess.join()
    # cal()
