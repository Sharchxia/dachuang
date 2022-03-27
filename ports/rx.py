import ports
from ports import *


def check_wrong(func):  # 语法糖，避免串口未开启却去调用读取数据的函数
    def wrong():
        try:
            ports.ser.isOpen()
        except Exception as e:
            print(e)
            return
        func()
    return wrong()


# def flexible(thread_name:str,start_bits:str, useful_code_length:int, useful_code_begin:int, num_of_useful) -> Any:
#     if ports.THREAD_POOL[thread_name]:
#         pass
#     else:
#         th = threading.Thread(target=read_flexible,args=(start_bits, useful_code_length, useful_code_begin, num_of_useful))
#         ports.THREAD_POOL[thread_name] = th
#         th.start()
#         th.join(5000)
#         return th.result


@check_wrong
def read_flexible(start_bits:str, useful_code_length:int, useful_code_begin:int, num_of_useful) -> Any:
    flag = True
    pool = []
    while flag:
        ports.ser.read_until(start_bits.encode('utf-8'))
        ports.ser.read(useful_code_begin-1)
        for i in range(num_of_useful):
            pool.append(str(ports.ser.read(useful_code_length).hex()))
        flag = False
    return pool


# def read_angle_euler() -> Dict[str,float]:
#     if ports.angle_euler_th is None:
#         ports.angle_euler_th = threading.Thread(target=angle_euler)  # 设置线程
#     try:
#         if not ports.angle_euler_th.is_alive():
#             ports.angle_euler_th.start()
#             ports.angle_euler_th.join(5000)
#             return ports.angle_euler_th.result
#     except:
#         print('thread initialized wrongly')


@check_wrong
def angle_euler() -> Dict[str,float]:
    flag = True
    operationCode = None
    usefulCode1 = None
    usefulCode2 = None
    usefulCode3 = None
    while flag:
        ports.ser.read_until(b'\xaa').hex()  # 判断帧头
        if ports.ser.read().hex() == b'\x55'.hex():  # 判断帧头
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x03'.hex():
            ports.ser.read()  # 忽略有效数据长度位
            usefulCode1 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode2 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode3 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            flag = False
    return {'pianhang':usefulCode1,'fuyang':usefulCode2,'gunzhuan':usefulCode3}


# def read_angle_speed() -> Dict[str,float]:
#     if ports.angle_speed_th is None:
#         ports.angle_speed_th = threading.Thread(target=angle_speed)  # 设置线程
#     try:
#         if not ports.angle_speed_th.is_alive():
#             ports.angle_speed_th.start()
#             ports.angle_speed_th.join(5000)
#             return ports.angle_speed_th.result
#     except:
#         print('thread initialized wrongly')


@check_wrong
def angle_speed() -> Dict[str,float]:
    flag = True
    operationCode = None
    usefulCode1 = None
    usefulCode2 = None
    usefulCode3 = None
    while flag:
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x04'.hex():
            ports.ser.read()
            usefulCode1 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode2 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode3 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            flag = False
    return {'pianhang':usefulCode1,'fuyang':usefulCode2,'gunzhuan':usefulCode3}


# def read_angle_acc() -> Dict[str,float]:
#     if ports.angle_acc_th is None:
#         ports.angle_acc_th = threading.Thread(target=angle_acc)
#     try:
#         if not ports.angle_acc_th.is_alive():
#             ports.angle_acc_th.start()
#             ports.angle_acc_th.join(5000)
#             return ports.angle_acc_th.result
#     except:
#         print('thread initialized wrongly')


@check_wrong
def angle_acc() -> Dict[str,float]:
    flag = True
    operationCode = None
    usefulCode1 = None
    usefulCode2 = None
    usefulCode3 = None
    while flag:
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x05'.hex():
            ports.ser.read()
            usefulCode1 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode2 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode3 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            flag = False
    return {'pianhang':usefulCode1,'fuyang':usefulCode2,'gunzhuan':usefulCode3}


# def read_light() -> Dict[str, int]:
#     if ports.light_status_th is None:
#         ports.light_status_th = threading.Thread(target=light_status)
#     try:
#         if not ports.light_status_th.is_alive():
#             ports.light_status_th.start()
#             ports.light_status_th.join(5000)
#             return ports.light_status_th.result
#     except:
#         print('thread initialized wrongly')


@check_wrong
def light_status() -> Dict[str, int]:
    flag = True
    operationCode = None
    usefulCode0 = None
    usefulCode1 = None
    usefulCode2 = None
    usefulCode3 = None
    usefulCode4 = None
    while flag:
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x08'.hex():
            ports.ser.read()
            usefulCode0 = convert_to_unsigned8(origin=str(ports.ser.read().hex()))
            usefulCode1 = convert_to_unsigned8(origin=str(ports.ser.read().hex()))
            usefulCode2 = convert_to_unsigned8(origin=str(ports.ser.read().hex()))
            usefulCode3 = convert_to_unsigned8(origin=str(ports.ser.read().hex()))
            usefulCode4 = convert_to_unsigned8(origin=str(ports.ser.read().hex()))
            flag = False
    return {'up':usefulCode0,'right':usefulCode1,'down':usefulCode2,'left':usefulCode3,'center':usefulCode4}


# def read_source_storage() -> int:
#     if ports.source_storage_th is None:
#         ports.source_storage_th = threading.Thread(target=source_storage)
#     try:
#         if not ports.source_storage_th.is_alive():
#             ports.source_storage_th.start()
#             ports.source_storage_th.join(5000)
#             return ports.source_storage_th.result
#     except:
#         print('thread initialized wrongly')


@check_wrong
def source_storage() -> int:
    flag = True
    operationCode = None
    usefulCode = None
    while flag:
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x00'.hex():
            ports.ser.read()
            usefulCode = convert_to_int(origin=str(ports.ser.read().hex()))
            flag = False
    return usefulCode


# def read_temper_status() -> Dict[str, float]:
#     if ports.temper_status_th is None:
#         ports.temper_status_th = threading.Thread(target=temper_status)
#     try:
#         if not ports.temper_status_th.is_alive():
#             ports.temper_status_th.start()
#             ports.temper_status_th.join(5000)
#             return ports.temper_status_th.result
#     except:
#         print('thread initialized wrongly')


@check_wrong
def temper_status() -> Dict[str, float]:
    flag = True
    operationCode = None
    usefulCode1 = None
    usefulCode2 = None
    usefulCode3 = None
    usefulCode4 = None
    usefulCode5 = None
    while flag:
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x02'.hex():
            ports.ser.read()
            usefulCode1 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode2 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode3 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode4 = convert_to_float(origin=str(ports.ser.read(4).hex()))
            usefulCode5 = 1 if ports.ser.read().hex == b'\x01' else 0
            flag = False
    return {'zhukong':usefulCode1,'zitai':usefulCode2,'dianyuan':usefulCode3,'rekong':usefulCode4,'re_on_off':usefulCode5}
