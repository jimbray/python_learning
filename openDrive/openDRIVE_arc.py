
# 高精地图圆弧部分 参数：
# s = "2.6661204800376140e+01"
# x = "5.5779610165223573e+01"
# y = "-1.4083929379520304e+01"
# hdg = "-4.3684380690538838e-01"
# length = "5.0000000000000014e+01" >
# < arc curvature = "8.0978518504482233e-02" / >

# 输入参数2个：弧长（length） 半径（radius）, 圆弧方向（顺时针为-，逆时针为 +）
# 输出参数6个： s  x y hdg length curvature
# 曲率 顺时针为负，逆时针为正

import math

# 预先定义 输入参数
# x/y 坐标系， x 右正左负，y上正下负
# param1: length
# param2: radius
# param3: 曲率的正负号 (看 弧度的方向:顺时针为 -1, 逆时针为 1 )
# param4: x 在计算过程中，累计之前的正负号  (看 本段 x 终点相对于 起点的 位置变化, 针对 x 轴)
# param5: y 在计算过程中，累计之前的正负号 （看本段 y 终点相对于起点的位置变化，针对 y轴）
input_tuple = [(2.09439*2, 4, -1, 1, -1),
               (2.09439*2, 4, 1, 1, -1),
               (6.28317*2, 4, 1, 1, -1),
               (2.09439*2, 4, 1, -1, 1),
               (2.09439*2, 4, -1, -1, -1)]
total_length = 0


def startCalArc(pre_info_tuple=None, sec_num=0):

    length = input_tuple[sec_num][0]
    radius = input_tuple[sec_num][1]
    arc_direction = input_tuple[sec_num][2]
    x_direction = input_tuple[sec_num][3]
    y_direction = input_tuple[sec_num][4]

    if sec_num == 0:
        s = 0
        x = 0
        y = 0
        hdg = 0
        curvature = (1 / radius) * arc_direction
        center_angle = length / radius
    else:
        s_pre, x_pre, y_pre, hdg_pre, length_pre, curvature_pre, radius_pre, center_angle_pre, arc_direction_pre = pre_info_tuple
        s = s_pre + length_pre
        x = x_direction * (radius_pre * math.sin(center_angle_pre)) + x_pre
        y = y_direction * (radius_pre - radius_pre * math.cos(center_angle_pre)) + y_pre
        hdg = hdg_pre + (center_angle_pre * arc_direction_pre)
        curvature = (1 / radius) * arc_direction
        center_angle = length / radius

    global total_length
    total_length = total_length + length
    params = (s, x, y, hdg, length, curvature, radius, center_angle, arc_direction)
    # print(params)

    print('<geometry s="%.4f" x="%.4f" y="%.4f" hdg="%.4f" length="%.4f">\n<arc curvature="%.4f"/>\n</geometry>' % (s, x, y, hdg, length, curvature))

    sec_num = sec_num + 1
    if sec_num < len(input_tuple):
        startCalArc(params, sec_num)
    else:
        print("total length : %.4f" % total_length)


if __name__ == '__main__':
    startCalArc()
