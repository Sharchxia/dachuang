from ports import *

def convert_to_float(origin:str, small=True) -> float:
    num = 0
    try:
        if small:
            num = struct.unpack('<f',bytes.fromhex(origin))[0]  # 小端转换
        else:
            num = struct.unpack('>f',bytes.fromhex(origin))[0]  # 大段转换
    except Exception as e:
        print(e)
    return num


def convert_to_unsigned8(origin:str, small=True) -> int:
    num = 0
    try:
        if small:
            num = struct.unpack('<B',bytes.fromhex(origin))[0]  # 小段转换
        else:
            num = struct.unpack('>B',bytes.fromhex(origin))[0]  # 大段转换
    except Exception as e:
        print(e)
    return num


def convert_to_int(origin:str, small=True) -> int:
    num = 0
    try:
        if small:
            num = struct.unpack('<i',bytes.fromhex(origin))[0]  # 小段转换
        else:
            num = struct.unpack('>i',bytes.fromhex(origin))[0]  # 大段转换
    except Exception as e:
        print(e)
    return num