from typing import Any
import time
import ports.var as var

def check_wrong(func) -> Any:  # 语法糖，避免串口未开启却去调用读取数据的函数
    def my_wrong(*args,**kwargs):
        try:
            if type(var.PORT) == 'serial.serialwin32.Serial':
                pass
            else:
                print('\033[1;31mERROR:','Please check the connection\033[0m')
                return
        except Exception as e:
            print('\033[1;31mERROR:\033[0m '+str(e))
            return
        res = func(*args,**kwargs)
        return res
    return my_wrong

def time_limitation(func) -> Any:
    def limit():
        var.TTT_start = time.time()
        res = func()
        return res
    return limit

def send_start_bits(func) -> Any:
    def begin(*args,**kwargs):
        var.PORT.write(b'\xaa')
        var.PORT.write(b'\x55')
        res = func(*args,**kwargs)
        return res
    return begin

def send_stop_bits(func) -> Any:
    def end(*args,**kwargs):
        res = func(*args,**kwargs)
        var.PORT.write(b'\x00')
        var.PORT.write(b'\x0a')
        var.PORT.write(b'\x0d')
        return res
    return end

def if_send_successfully(func) -> bool:
    def check(*args,**kwargs):
        try:
            func(*args,**kwargs)
            return True
        except Exception as e:
            if str(e) == 'Attempting to use a port that is not open':
                pass
            else:
                print('\033[1;31mERROR:\033[0m',e)
            return False
    return check()
