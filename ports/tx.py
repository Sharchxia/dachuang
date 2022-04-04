from ports.my_decorator import check_wrong as wrong
from ports.my_decorator import send_start_bits as start
from ports.my_decorator import send_stop_bits as stop
# from ports.my_decorator import if_send_successfully as check
# from ports.convert import convert_to_float  # 二进制形式的32位字符串转换位32为float型
# from ports.convert import convert_to_int  # 二进制形式的32位字符串转换为32位int型
# from ports.convert import convert_to_unsigned8  # 二进制形式的8位字符串转换为8位unsigned int型
from ports.convert import convert_uint8_to_bytes
from ports.convert import convert_float32_to_bytes
from ports.convert import convert_ushort_to_bytes
# from ports.convert import convert_string_to_bytes
# from ports.convert import convert_bytes_to_string
import ports.var as var

# 经测试发现，对卫星的写操作： 要求每次写之间间隔一定的时间，否则会造成指令发送失败，即指令不执行
# 在卫星开机时，应调用一次 open_all()函数，此后才可保证读与写功能正常

@wrong
@start
@stop
def close_all():  # 未测试且建议不要用
    data = [b'\x00',b'\x01',b'\x00']
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 已测试
def source_control(n0=1,n1=1,n2=1,n3=1,n4=1,n5=1,n6=1,n7=1,n8=1,n9=1):
    c0 = b'\x00' if n0==0 else b'\x01'
    c1 = b'\x00' if n1==0 else b'\x01'
    c2 = b'\x00' if n2==0 else b'\x01'
    c3 = b'\x00' if n3==0 else b'\x01'
    c4 = b'\x00' if n4==0 else b'\x01'
    c5 = b'\x00' if n5==0 else b'\x01'
    c6 = b'\x00' if n6==0 else b'\x01'
    c7 = b'\x00' if n7==0 else b'\x01'
    c8 = b'\x00' if n8==0 else b'\x01'
    c9 = b'\x00' if n9==0 else b'\x01'
    # data = [b'\xaa',b'\x55',b'\x02',b'\x0a',c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,b'\x00',b'\x0a',b'\x0d']
    data = [b'\x02',b'\x0a',c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 已测试
def wheel_control(switch=1):
    c = b'\x00' if switch==0 else b'\x01'
    data = [b'\x04',b'\x01',c]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 已测试
def temp_control(switch=1):
    c = b'\x00' if switch==0 else b'\x01'
    data = [b'\x06',b'\x01',c]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 已测试
def magnetic_control(switch=1):
    c = b'\x00' if switch==0 else b'\x01'
    data = [b'\x08',b'\x01',c]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 已测试
def wheel_speed_control(speed=0,direction=True):  # speed>=0 and direction=True,正转；speed<0 and direction=True,反转；
    direction = direction if speed>=0 else not direction
    speed = abs(speed)%101
    speed = convert_uint8_to_bytes(speed)
    c = b'\x00' if direction is False else b'\x01'
    data = [b'\x0a',b'\x02',speed,c]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 已测试
def temp_set(main_panel:float,gesture:float,source:float,hot:float):
    main_panel = convert_float32_to_bytes(main_panel)
    gesture = convert_float32_to_bytes(gesture)
    source = convert_float32_to_bytes(source)
    hot = convert_float32_to_bytes(hot)
    data = [b'\x0c',b'\x10',main_panel,gesture,source,hot]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 已测试
def magnetic_magnitude(x_axis:int,y_axis:int,x_moment=True,y_moment=True):  # True 代表磁矩为正
    x_axis = 0 if x_axis<=0 else x_axis%101
    y_axis = 0 if y_axis<=0 else y_axis%101
    x_axis = convert_uint8_to_bytes(x_axis)
    y_axis = convert_uint8_to_bytes(y_axis)
    x_moment = b'\x01' if x_moment else b'\x00'
    y_moment = b'\x01' if y_moment else b'\x00'
    data = [b'\x0e',b'\x04',x_axis,y_axis,x_moment,y_moment]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 暂不清楚具体功能，所以未测试
def temp_corresponding(main_panel:int, gesture:int, source:int, hot:int):
    main_panel = 0 if main_panel<0 else main_panel%8
    gesture = 0 if gesture<0 else gesture%8
    source = 0 if source<0 else source%8
    hot = 0 if hot<0 else hot%8
    main_panel = convert_uint8_to_bytes(main_panel)
    gesture = convert_uint8_to_bytes(gesture)
    source = convert_uint8_to_bytes(source)
    hot = convert_uint8_to_bytes(hot)
    data = [b'\x10',b'\x04',main_panel,gesture,source,hot]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 暂不清楚具体功能，所以未测试
def heat_corresponding(main_panel:int, gesture:int, source:int, hot:int):
    main_panel = 0 if main_panel<0 else main_panel%8
    gesture = 0 if gesture<0 else gesture%8
    source = 0 if source<0 else source%8
    hot = 0 if hot<0 else hot%8
    main_panel = convert_uint8_to_bytes(main_panel)
    gesture = convert_uint8_to_bytes(gesture)
    source = convert_uint8_to_bytes(source)
    hot = convert_uint8_to_bytes(hot)
    data = [b'\x12',b'\x04',main_panel,gesture,source,hot]
    for i in data:
        var.PORT.write(i)

@wrong
@start
@stop  # 已测试
def steering_angle(two=0, four=0, one=0, three=0):  # 设备两侧的帆板所用舵机为2和4；1、3无用
    one = 0 if one<0 else one%8
    two = 0 if two<0 else two%8
    three = 0 if three<0 else three%8
    four = 0 if four<0 else four%8
    one = convert_uint8_to_bytes(one)
    two = convert_uint8_to_bytes(two)
    three = convert_uint8_to_bytes(three)
    four = convert_uint8_to_bytes(four)
    data = [b'\x14',b'\x04',one,two,three,four]
    for i in data:
        var.PORT.write(i)


@wrong
@start
@stop  # 未测试代码，尽量不要使用
def communicate(number:int,content:str) -> bool:
    number = 0 if number<0 else number %256
    num = convert_ushort_to_bytes(number)
    N = len(content) + 2
    content = content.encode('utf-8')
    N = convert_uint8_to_bytes(N)
    data = [b'\x16',N,num, content]
    for i in data:
        var.PORT.write(i)
    return True

@wrong  # 在卫星开机后执行一下这个，保证数据传输
def open_all():
    source_control()
    wheel_control()
    temp_control()
    magnetic_control()
