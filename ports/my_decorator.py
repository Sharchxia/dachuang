import ports
from ports import *


def check_wrong(func) -> Any:  # 语法糖，避免串口未开启却去调用读取数据的函数
    def my_wrong(*args,**kwargs):
        try:
            if type(ports.ser) == 'serial.serialwin32.Serial':
                pass
            else:
                print('ERROR:','Please check the connection')
                return
        except Exception as e:
            print('ERROR: '+str(e))
            return
        res = func(*args,**kwargs)
        return res
    return my_wrong

def time_limitation(func) -> Any:
    def limit():
        ports.TTT_start = time.time()
        res = func()
        return res
    return limit

def send_start_bits(func) -> Any:
    def begin(*args,**kwargs):
        ports.ser.write(b'\xaa')
        ports.ser.write(b'\x55')
        res = func(*args,**kwargs)
        return res
    return begin

def send_stop_bits(func) -> Any:
    def end(*args,**kwargs):
        res = func(*args,**kwargs)
        ports.ser.write(b'\x00')
        ports.ser.write(b'\x0a')
        ports.ser.write(b'\x0d')
        return res
    return end

def if_send_successfully(func) -> bool:
    def check(*args,**kwargs):
        try:
            func(*args,**kwargs)
            return True
        except Exception as e:
            print('ERROR',e)
            return False
    return check()
