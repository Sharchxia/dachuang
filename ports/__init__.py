import serial
from serial.tools import list_ports
from threading import Thread
import time
import struct

class Receive:
    def __init__(self, port=None, baud_rate=9600, timeout=3, read_num=6, read_t='int'):
        self.port = port  # 串口名称
        self.baud = baud_rate  # 波特率
        self.time = timeout  # 超时时间
        self.__connection = None  # 串口对象
        self.__read_thread = None  # 线程对象
        self.__read_flag = True  # 控制线程,因为线程为死循环，要停止线程就设置标志位中断线程
        self.read_start = 'aaaa'
        self.read_type = read_t  # 读取数据的类型
        self.list = self.list()  # 列出所有可用串口
        self.read_number = read_num  # 每次读的处理后的数据长度
        self.data = None  # 读取出的数据
        self.__get_flag = False  # 是否可读，保护线程

    def get(self):  # 向外部返回数据
        if self.__get_flag:
            return self.data  # 保护线程，保证读数据不和内部线程获取数据冲突
        else:
            print('\033[0;32mNo data is available\033[0m')

    def list(self, length=4):  # 设置切割串口名称的长度，返回所有串口的列表，如果为0则不对名称进行切割
        portL = list_ports.comports()
        if len(portL) == 0:
            print('\033[0;32mNo ports available\033[0m')  # 没串口的情况
            return []
        else:
            for i in range(len(portL)):
                if length:
                    portL[i] = str(portL[i])[:length]
                else:
                    portL[i] = str(portL[i])
            self.list = portL
            return portL

    def connect(self, port=None, baud_rate=9600, timeout=3):  # 连接串口
        if port is None and self.port is None:
            print('\033[0;32mWrongly, no port is selected\033[0m]')
            return
        self.baud = baud_rate if baud_rate != self.baud else self.baud
        self.time = timeout if timeout != self.time else self.time
        self.port = port if port is not self.port else self.port
        self.__connection = serial.Serial(self.port, baudrate=self.baud, timeout=self.time)
        self.__get_flag = False

    def read(self, start='aaaa', object_type='int', number=6):  # 从缓冲区中读取数据并处理，这里是关闭原有读取线程，新开一个
        if self.__connection is None:
            print('\033[0;32m Please first connect to a port\033[0m')
            return
        self.read_start = start if start != self.read_start else self.read_start
        self.read_type = object_type if object_type!= self.read_type else self.read_type
        self.__read_num(number)

        self.stop_read()  # 停止线程，即，使线程死循环被跳出

        self.__read_thread = Thread(target=self.__read)  # 开启新线程
        self.__read_thread.start()
        # self.__read_thread.join()

    def __read_num(self, number=6):  # 设置读取数据的个数
        self.read_number = number if number != self.read_number else self.read_number

    def __read(self):  # 线程target，每一次循环为保证线程对资源的调用不冲突，会暂停300ms让数据可以被返回出外部
        while self.__read_flag:
            self.__get_flag = True
            time.sleep(.3)  # 暂停300ms只有这段时间get函数可以向外部返回数据
            self.__get_flag = False
            data = []
            self.__connection.read_until(self.read_start.encode('utf-8'))  # 每段数据的开始，这段数据默认没有实际处理意义
            if not self.__read_flag:
                break
            if self.read_type == 'int':  # 读取32位整型数据
                for i in range(self.read_number):  # 读取设定好个数的数据
                    d = self.__connection.read(4).hex()  # 4个字节的整型的16进制转换后的字符串
                    # print(d)
                    if len(d) == 8:  # 保证数据可用，因为串口有3秒的超时，所以可能不会获得有效数据
                        d = self.__convert_to_int(d)
                        # print(d)
                        data.append(d)
                while len(data) < self.read_number:
                    data.append(0)  # 是每次返回的数据个数符合要求
                self.data = data  # 存入类变量，get函数通过访问该变量向外界返回数据

    def stop_read(self):  # 使线程相对安全的停止，不用join是为了防止target函数异常退出
        if self.__read_thread is not None:
            self.__read_flag = False
            time.sleep(0.4)
            self.__read_flag = True
            self.__get_flag = False

    @staticmethod  # 类函数，将符合要求的字符串转为32位整型数字
    def __convert_to_int(origin: str, small=True) -> int:  # 输入要求是长度为8的代表16进制的字符串
        num = 0
        try:
            if small:
                num = struct.unpack('<i', bytes.fromhex(origin))[0]  # 小端转换
            else:
                num = struct.unpack('>i', bytes.fromhex(origin))[0]  # 大端转换
        except Exception as e:
            print('ERROR:', e)
        return num

if __name__ == '__main__':
    r = Receive()
    po = r.list
    print(po)
    r.connect(po[0])
    r.read()
    while True:
        print(r.get())
        print(r.data)