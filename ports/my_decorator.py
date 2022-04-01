import ports
from ports import *


def check_wrong(func) -> Any:  # 语法糖，避免串口未开启却去调用读取数据的函数
    def my_wrong():
        try:
            if type(ports.ser) == 'serial.serialwin32.Serial':
                pass
        except Exception as e:
            print('ERROR: '+str(e))
            return
        res = func()
        return res
    return my_wrong

def time_limitation(func) -> Any:
    def limit():
        ports.TTT_start = time.time()
        res = func()
        return res
    return limit

def send_start_bits(func) -> Any:
    def begin():
        ports.ser.write(b'\xaa')
        ports.ser.write(b'\x55')
        res = func()
        return res
    return begin

def send_stop_bits(func) -> Any:
    def end():
        res = func()
        ports.ser.write(b'\x00')
        ports.ser.write(b'\x0a')
        ports.ser.write(b'\x0d')
        return res
    return end
