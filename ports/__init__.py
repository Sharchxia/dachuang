import serial
from serial.tools import list_ports
from typing import List
from typing import Dict
from typing import Any
from typing import Union
import threading
import struct
from concurrent.futures import ThreadPoolExecutor
import time

import ports.port_init
import ports.rx
import ports.tx

THREAD_POOL = {}  # 灵活线程池

ser = None  # 端口的声明
TTT_start = None  # 计时器
TTT_end = None  # 计时器

# 用于外部调用函数的函数名

port_list = ports.port_init.port_list  # 列出可用端口
port_set = ports.port_init.port_set  # 设置用于通信的端口
port_test = ports.port_init.port_test  # 测试端口是否连通
baud_set = ports.port_init.baud_set  # 波特率的设置，需先将端口连接

# 接收所属部分
angle_euler = ports.rx.angle_euler  # 返回欧拉角的值
angle_speed = ports.rx.angle_speed  # 返回角速度的值
angle_acc = ports.rx.angle_acc  # 返回角加速度的值
light_status = ports.rx.light_status  # 返回太敏数据
source_storage = ports.rx.source_storage  # 返回电池电量
temper_status = ports.rx.temper_status  # 返回各个板层的温度及热控是否打开

# 发送所属部分
close_all = ports.tx.close_all  # 关闭所有
source_control = ports.tx.source_control  # 电源控制开关
wheel_control = ports.tx.wheel_control  # 飞轮控制开关
temp_control = ports.tx.temp_control  # 温度控制开关
magnetic_control = ports.tx.magnetic_control  # 磁力矩控制开关
wheel_speed = ports.tx.wheel_speed_control  # 飞轮转速设置
temp_set = ports.tx.temp_set  # 模块温度设置
magnetic_magnitude = ports.tx.magnetic_magnitude  # 磁矩大小设置
temp_corresponding = ports.tx.temp_corresponding  # 设置温度对应关系
heat_corresponding = ports.tx.heat_corresponding  # 设置加热对应关系
steering_angle = ports.tx.steering_angle  # 舵机角度
