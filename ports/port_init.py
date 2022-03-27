import ports
from ports import *


def port_list() -> List[str]:  # 返回可用端口的列表
    try:
        ports.ser.close()
        ports.ser = None
    except:
        pass
    portL = list_ports.comports()
    if len(portL) == 0:
        return []
        print('No ports available')
    else:
        return list(portL)


def port_set(port_name:str) -> None:
    if port_name:
        ports.ser = serial.Serial(port_name,115200,timeout=3)
    else:
        print('No such port')
        pass


def baud_set(rate:int) -> None:
    try:
        port.ser.baudrate = rate
    except:
        print('Please connect the port first')
        pass


def port_test() -> bool:
    try:
        if ports.ser.isopen():
            return True
    except:
        pass
    return False
