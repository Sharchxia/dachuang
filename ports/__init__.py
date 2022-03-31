import serial
from serial.tools import list_ports
from typing import List
from typing import Dict
from typing import Any
import threading
import struct
from concurrent.futures import ThreadPoolExecutor
import time

import ports.port_init
import ports.rx
import ports.tx
import ports.convert
# import ports.my_decorator

THREAD_POOL = {}  # 灵活线程池

ser = None  # 端口的声明
TTT_start = None  # 计时器
TTT_end = None  # 计时器
# # 各个线程的初始声明
# angle_euler_th = None
# angle_speed_th = None
# angle_acc_th = None
#
# source_storage_th = None
#
# temper_status_th = None
#
# light_status_th = None
#
# write_th = None
# # 修饰器
# wrong = ports.my_decorator.check_wrong  # 保证ser端口初始化，否则不执行其后代码，防止错误
# TTT = ports.my_decorator.time_limitation  # 开始时间戳
# start = ports.my_decorator.send_start_bits  # 发送帧头
# stop = ports.my_decorator.send_stop_bits  # 发送帧尾
# 用于外部调用函数的函数名
convert_to_float = ports.convert.convert_to_float  # 二进制形式的32位字符串转换位32为float型
convert_to_int = ports.convert.convert_to_int  # 二进制形式的32位字符串转换为32位int型
convert_to_unsigned8 = ports.convert.convert_to_unsigned8  # 二进制形式的8位字符串转换为8位unsigned int型
convert_uint8_to_bytes = ports.convert.convert_uint8_to_bytes
convert_float32_to_bytes = ports.convert.convert_float32_to_bytes
convert_string_to_bytes = ports.convert.convert_string_to_bytes
convert_bytes_to_string = ports.convert.convert_bytes_to_string

port_list = ports.port_init.port_list  # 列出可用端口
port_set = ports.port_init.port_set  # 设置用于通信的端口
port_test = ports.port_init.port_test  # 测试端口是否连通
baud_set = ports.port_init.baud_set  # 波特率的设置，需先将端口连接

angle_euler = ports.rx.angle_euler  # 返回欧拉角的值
angle_speed = ports.rx.angle_speed  # 返回角速度的值
angle_acc = ports.rx.angle_acc  # 返回角加速度的值
light_status = ports.rx.light_status  # 返回太敏数据
source_storage = ports.rx.source_storage  # 返回电池电量
temper_status = ports.rx.temper_status  # 返回各个板层的温度及热控是否打开
