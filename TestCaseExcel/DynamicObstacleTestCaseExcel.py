#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: DynamicObstacleTestCaseExcel.py
@time: 2019/03/09
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
obstacle_type_list = ["行人", "低速车", "同速车", "高速车"]
print(obstacle_type_list)

# 障碍物方向
obstacle_direction_list = ["同向", "逆向"]
print(obstacle_direction_list)

# 障碍物方向 相对车头中心
obstacle_angle_list = [0, 30, 60, 90]
print(obstacle_angle_list)

# 障碍物材质
obstacle_material_list = ["塑料", "石材", "金属", "玻璃"]
print(obstacle_material_list)

# 环境能见度 5m ~ 100m
environment_visibility = list(range(50, 501, 50))
print(environment_visibility)

# 天气
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

# 风速与车头中心夹角
wind_angle_list = [0, 30, 60, 90]
print(wind_angle_list)

# 风速
# wind_speed_list = list(range(0, 37, 3))
wind_speed_list = [5, 20]
print(wind_speed_list)

# 是否有超车条件
is_overtake_list = ["有", "无"]
print(is_overtake_list)

# 列的内容对应应该插入的列的位置
content_line_num_list = [3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def writeByPart(sheet, part_list):
    # 分批写入
    # 每次 5k 条
    part = len(part_list) // 5000
    last_part = len(part_list) % 5000
    print("part: " + str(part))
    for part_index in range(0, part):
        start = 0
        if part_index > 0:
            start = 1
        print("[" + str((5000 * part_index + start)) + "]-[" + str(5000 * (part_index + 1)) + "]")
        for row in range(5000 * part_index + start, 5000 * (part_index + 1)):
            line = part_list[row]
            # 根据字典写入对应列
            for column in range(0, len(line)):
                # sheet.write(row + 2, column + 3, line[column], set_style("style", 220))
                sheet.write(row + 2, content_line_num_list[column], line[column], set_style("style", 220))

    # # 还有最后一波
    # print("last part : [" + str((5000 * part + 1)) + "]-[" + str(5000 * part + last_part) + "]")
    # sheet.write((5000 * part + 1) + 2, (5000 * part + last_part) + 3, line[(5000 * part + last_part)],
    #             set_style("style", 220))


def writeByFile(total_list, file_name, sheet_index):

    xlsx = xlwt.Workbook(encoding='UTF-8', style_compression=2)
    print("-"*25 + file_name + "-"*25)
    sheet = xlsx.add_sheet("TestCase")

    # 添加表头
    first_sheet_header_dic = {0: "用例ID", 1: "用例名称", 2: "测试场景", 3: "前置条件", 13: "障碍物大小", 21: "优先级", 22: "重要级",
                              23: "预期结果", 29: "实际结果", 35: "备注", 36: "执行人", 37: "执行日期"}
    second_sheet_header_dic = {3: "无人车设定的最高速度(km/h)", 4: "无人车载重(kg)", 5: "无人车行驶轨迹", 6: "道路坡度(角度)",
                               7: "障碍物类型", 8: "障碍物方向（相对车头中心）", 9: "障碍物与中心夹角 单位：角度",
                               10: "障碍物加速度 单位：m/s² ", 11: "障碍物与车体相对速度 单位 m/s", 12: "障碍物材质",
                               13: "长", 14: "宽", 15: "高", 16: "环境能见度(m)", 17: "天气",
                               18: "昼夜", 19: "风速方向（相对车头中心）", 20: "风速与中心夹角 单位：角度", 21: "风速（m/s）",
                               22: "是否有超车条件",
                               25: "减速开始距离（距离障碍物 单位:m）", 26: "停车完成时间 单位：s", 27: "加速开始距离（距离障碍物 单位：m）",
                               28: "超车完成时间（车身越过障碍物为准） 单位：s", 29: "是否返回原车道", 30: "无人车其他行为"
                               20: "减速开始距离（距离障碍物 单位:m）", 21: "停车距离（距离障碍物 单位:m）", 22: "无人车其他行为"}
    for k, v in first_sheet_header_dic.items():
        sheet.write(0, k, v, set_style("style", 220))

    for k, v in second_sheet_header_dic.items():
        sheet.write(1, k, v, set_style("style", 220))

    print("write by sheet -> [" + str(50000*sheet_index) + "-[" + str(50000*(sheet_index+1)) + "]")
    sheet_list = total_list[50000*sheet_index: 50000*(sheet_index+1)]
    writeByPart(sheet, sheet_list)

    xlsx.save(file_name + ".xls")
    print(file_name + "写入完成")


def writeList(list):
    sheet_count = len(list) // 50000 + 1
    print("sheet count -> " + str(sheet_count))
    for sheet_index in range(0, sheet_count):
        writeByFile(list, "静态障碍物测试用例-" + str(sheet_index+1), sheet_index)


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
    xlsx.save("静态障碍物测试用例设计.xls")
    print("文件写入完成")


def cal():
    # 对应的列
    ["无人车设定的最高时速（km/h）", "无人车载重(kg)", "无人车行驶轨迹", "道路坡度(角度)", "障碍物材质", "环境能见度(m)",
     "天气", "昼夜", "风速方向（相对车头中心）", "风速（m/s）", "是否有超车条件"]
    # 列的内容 对应 应该插入的 列的column数
    # {0: 3, 1: 4, 2: 5, 4: 6, 5: 10, 6: 11, 7: 12, 8: 13, 9: 14, 10: 15, 11: 16}

    result = list(itertools.product(vehicle_speed_list, vehicle_load_weight_list,
                                    vehicle_driving_track_list, vehicle_road_slope_list,
                                    obstacle_material_list,
                                    environment_visibility, weather_type_list, day_and_night_list,
                                    wind_direction_list, wind_speed_list, is_overtake_list))
    print("list size: " + str(len(result)))
    # print(result)
    writeList(result)
    # writeExcel(result)
    # print(list(itertools.permutations(["ABCD", "123"], 2)))
    # print(list(itertools.product(["ABCD", "123"], 2)))


if __name__ == '__main__':
    cal_precess = Process(target=cal)
    cal_precess.start()
    cal_precess.join()
