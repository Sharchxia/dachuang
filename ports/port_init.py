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
    try:
        if port_name:
            ports.ser = serial.Serial(port_name,115200,timeout=3,stopbits=2)
        else:
            print('Please assign correct port')
    except:
        print('There is no such port.')



def baud_set(rate:int) -> None:
    try:
        port.ser.baudrate = rate
    except:
        print('Please connect the port first')
        pass


def port_test() -> bool:
    try:
        if ports.ser.is_open():
            return True
    except:
        pass
    return False
