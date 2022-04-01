from ports import *

def convert_to_float(origin:str, small=True) -> float:
    num = 0
    try:
        if small:
            num = struct.unpack('<f',bytes.fromhex(origin))[0]  # 小端转换
        else:
            num = struct.unpack('>f',bytes.fromhex(origin))[0]  # 大段转换
    except Exception as e:
        print('ERROR:',e)
    return num

def convert_to_unsigned8(origin:str, small=True) -> int:
    num = 0
    try:
        if small:
            num = struct.unpack('<B',bytes.fromhex(origin))[0]  # 小段转换
        else:
            num = struct.unpack('>B',bytes.fromhex(origin))[0]  # 大段转换
    except Exception as e:
        print('ERROR:',e)
    return num

def convert_to_int(origin:str, small=True) -> int:
    num = 0
    try:
        origin = origin+6*'0'
        if small:
            num = struct.unpack('<i',bytes.fromhex(origin))[0]  # 小段转换
        else:
            num = struct.unpack('>i',bytes.fromhex(origin))[0]  # 大段转换
    except Exception as e:
        print('ERROR:',e)
    return num

def convert_uint8_to_bytes(origin:int,small=True) -> bytes:
    s = b''
    try:
        if small:
            s = struct.pack('<B', origin)
        else:
            s = struct.pack('>B', origin)
    except Exception as e:
        print('ERROR:',e)
    return s

def convert_float32_to_bytes(origin:float,small=True) -> bytes:
    s = b''
    try:
        if small:
            s = struct.pack('<f', origin)
        else:
            s = struct.pack('>f', origin)
    except Exception as e:
        print('ERROR:',e)
    return s

def convert_string_to_bytes(origin:str,small=True) -> bytes:  # 未完成代码，不要使用
    s = b''
    try:
        if small:
            s = struct.pack('<s', origin)
        else:
            s = struct.pack('>s', origin)
    except Exception as e:
        print('ERROR:',e)
    return s

def convert_bytes_to_string(origin:bytes,small=True) -> str:  # 未完成代码，不要使用
    s = ''
    try:
        if small:
            s = struct.unpack('<s', origin)
        else:
            s = struct.unpack('>s', origin)
    except Exception as e:
        print('ERROR:',e)
    return s
