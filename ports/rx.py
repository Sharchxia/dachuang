from ports.my_decorator import check_wrong as wrong
from ports.my_decorator import time_limitation as TTT
import ports
from ports import *
from ports.convert import convert_to_float  # 二进制形式的32位字符串转换位32为float型
from ports.convert import convert_to_int  # 二进制形式的32位字符串转换为32位int型
from ports.convert import convert_to_unsigned8  # 二进制形式的8位字符串转换为8位unsigned int型
# from ports.convert import convert_uint8_to_bytes
# from ports.convert import convert_float32_to_bytes
# from ports.convert import convert_string_to_bytes
# from ports.convert import convert_bytes_to_string
# from ports.convert import convert_ushort_to_bytes

@wrong
@TTT  # 未完成代码，不要使用
def read_flexible(start_bits: str, useful_code_length: int, useful_code_begin: int, num_of_useful) -> Any:
    flag = True
    pool = []
    while flag:
        ports.TTT_end = time.time()
        ports.ser.read_until(start_bits.encode('utf-8'))
        ports.ser.read(useful_code_begin - 1)
        for i in range(num_of_useful):
            pool.append(str(ports.ser.read(useful_code_length).hex()))
        flag = False
    return pool


@wrong
@TTT
def angle_euler() -> Dict[str, float]:
    flag = True
    operationCode = None
    usefulCode1 = 0
    usefulCode2 = 0
    usefulCode3 = 0
    while flag:
        ports.TTT_end = time.time()
        if ports.TTT_end - ports.TTT_start >=5:
            flag = False
        ports.ser.read_until(b'\xaa')  # 判断帧头
        if ports.ser.read().hex() == b'\x55'.hex():  # 判断帧头
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x03'.hex():
            ports.ser.read()  # 忽略有效数据长度位
            usefulCode1 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode2 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode3 = convert_to_float(origin=ports.ser.read(4).hex())
            flag = False
    data = {'pianhang': usefulCode1, 'fuyang': usefulCode2, 'gunzhuan': usefulCode3}
    return data


@wrong
@TTT
def angle_speed() -> Dict[str, float]:
    flag = True
    operationCode = None
    usefulCode1 = 0
    usefulCode2 = 0
    usefulCode3 = 0
    while flag:
        ports.TTT_end = time.time()
        if ports.TTT_end - ports.TTT_start >=5:
            flag = False
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x04'.hex():
            ports.ser.read()
            usefulCode1 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode2 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode3 = convert_to_float(origin=ports.ser.read(4).hex())
            flag = False
    data = {'pianhang': usefulCode1, 'fuyang': usefulCode2, 'gunzhuan': usefulCode3}
    return data


@wrong
@TTT
def angle_acc() -> Dict[str, float]:
    flag = True
    operationCode = None
    usefulCode1 = 0
    usefulCode2 = 0
    usefulCode3 = 0
    while flag:
        ports.TTT_end = time.time()
        if ports.TTT_end - ports.TTT_start >=5:
            flag = False
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x05'.hex():
            ports.ser.read()
            usefulCode1 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode2 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode3 = convert_to_float(origin=ports.ser.read(4).hex())
            flag = False
    data = {'pianhang': usefulCode1, 'fuyang': usefulCode2, 'gunzhuan': usefulCode3}
    return data


@wrong
@TTT
def light_status() -> Dict[str, int]:
    flag = True
    operationCode = None
    usefulCode0 = 0
    usefulCode1 = 0
    usefulCode2 = 0
    usefulCode3 = 0
    usefulCode4 = 0
    while flag:
        ports.TTT_end = time.time()
        if ports.TTT_end - ports.TTT_start >=5:
            flag = False
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x08'.hex():
            ports.ser.read()
            usefulCode0 = convert_to_unsigned8(origin=ports.ser.read().hex())
            usefulCode1 = convert_to_unsigned8(origin=ports.ser.read().hex())
            usefulCode2 = convert_to_unsigned8(origin=ports.ser.read().hex())
            usefulCode3 = convert_to_unsigned8(origin=ports.ser.read().hex())
            usefulCode4 = convert_to_unsigned8(origin=ports.ser.read().hex())
            flag = False
    data = {'up': usefulCode0, 'right': usefulCode1, 'down': usefulCode2, 'left': usefulCode3, 'center': usefulCode4}
    return data


@wrong
@TTT
def source_storage() -> int:
    flag = True
    operationCode = None
    usefulCode = 0
    while flag:
        ports.TTT_end = time.time()
        if ports.TTT_end - ports.TTT_start >=5:
            flag = False
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x00'.hex():
            ports.ser.read()
            usefulCode = convert_to_int(origin=ports.ser.read().hex())
            flag = False
    data = usefulCode
    return data


@wrong
@TTT
def temper_status() -> Dict[str, float]:
    flag = True
    operationCode = None
    usefulCode1 = 0
    usefulCode2 = 0
    usefulCode3 = 0
    usefulCode4 = 0
    usefulCode5 = 0
    while flag:
        ports.TTT_end = time.time()
        if ports.TTT_end - ports.TTT_start >=5:
            flag = False
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x02'.hex():
            ports.ser.read()
            usefulCode1 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode2 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode3 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode4 = convert_to_float(origin=ports.ser.read(4).hex())
            usefulCode5 = 1 if ports.ser.read().hex == b'\x01' else 0
            flag = False
    data = {'zhukong': usefulCode1, 'zitai': usefulCode2, 'dianyuan': usefulCode3, 'rekong': usefulCode4,
            're_on_off': usefulCode5}
    return data


@wrong
@TTT
def communicate() -> Dict[str, str]:  # 未完成代码，不要使用
    flag = True
    message = ''
    title = ''
    operationCode = None
    while flag:
        ports.TTT_end = time.time()
        if ports.TTT_end - ports.TTT_start >=5:
            flag = False
        ports.ser.read_until(b'\xaa')
        if ports.ser.read().hex() == b'\x55'.hex():
            operationCode = ports.ser.read().hex()
        if operationCode == b'\x01'.hex():
            num = convert_to_unsigned8(ports.ser.read().hex())
            title = ports.ser.read().decode('utf-8')
            title += ports.ser.read().decode('utf-8')
            for i in range(num - 2):
                message += ports.ser.read().decode('utf-8')
            flag = False
    data = {'bianhao': title, 'meg': message}
    return data
