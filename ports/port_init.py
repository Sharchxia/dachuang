import ports.var as var
import serial
from serial.tools import list_ports
from typing import List

def port_list() -> List[str]:  # 返回可用端口的列表，用户需自行对列表中的元素进行字符串切割获得可用名称
    try:
        var.PORT = serial.Serial()
    except:
        pass
    portL = list_ports.comports()
    if len(portL) == 0:
        return []
        print('No ports available')
    else:
        return list(portL)


def port_set(port_name:str) -> bool:
    try:
        if port_name:
            var.PORT = serial.Serial(port_name,115200,timeout=3,stopbits=2)
            return True
        else:
            return False
            print('Please assign correct port')
    except:
        print('\033[1;31mThere is no such port.\033[0m')
        return False



def baud_set(rate:int) -> None:  # 建议用来当摆设，可用
    try:
        var.PORT.baudrate = rate
    except:
        print('Please connect the port first')
        pass


# def port_test() -> bool:
#     try:
#         if PORT.is_open():
#             return True
#     except:
#         pass
#     return False
