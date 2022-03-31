import ports
from ports import *
from ports.my_decorator import check_wrong as wrong
from ports.my_decorator import send_start_bits as start
from ports.my_decorator import send_stop_bits as stop


@wrong
@start
@stop
def close_all():
    # data = [b'\xaa',b'\x55',b'\x00',b'\x01',b'\x00',b'\x00',b'\x0a',b'\x55']
    data = [b'\x00',b'\x01',b'\x00']
    for i in data:
        ports.ser.write(i)

@wrong
@start
@stop
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
        ports.ser.write(i)

@wrong
@start
@stop
def wheel_control(switch=1):
    c = b'\x00' if switch==0 else b'\x01'
    data = [b'\x04',b'\x01',c]
    for i in data:
        ports.ser.write(i)

@wrong
@start
@stop
def temp_control(switch=1):
    c = b'\x00' if switch==0 else b'\x01'
    data = [b'\x06',b'\x01',c]
    for i in data:
        ports.ser.write(i)

@wrong
@start
@stop
def magnetic_control(switch=1):
    c = b'\x00' if switch==0 else b'\x01'
    data = [b'\x08',b'\x01',c]
    for i in data:
        ports.ser.write(i)

@wrong
@start
@stop
def wheel_speed_control(direction=True,speed=0):  # speed>=0 and direction=True,正转；speed<0 and direction=True,反转；
    direction = direction if speed>=0 else not direction
    speed = abs(speed)%100
    speed = convert_uint8_to_bytes(speed)
    c = b'\x00' if direction is False else b'\x01'
    data = [b'\x0a',b'\x01',speed,c]
    for i in data:
        ports.ser.write(i)

@wrong
@start
@stop
def temp_set(main_panel:float,gesture:float,source:float,hot:float):
    main_panel = convert_float32_to_bytes(main_panel)
    gesture = convert_float32_to_bytes(gesture)
    source = convert_float32_to_bytes(source)
    hot = convert_float32_to_bytes(hot)
    data = [b'\x0c',b'\x10',main_panel,gesture,source,hot]
    for i in data:
        ports.ser.write(i)

@wrong
@start
@stop
def magnetic_magnitude(x_axis:int,y_axis:int,x_moment:bool,y_moment:bool):  # True 代表磁矩为正
    x_axis = 0 if x_axis<0 else x_axis%101
    y_axis = 0 if y_axis<0 else y_axis%101
    x_axis = convert_uint8_to_bytes(x_axis)
    y_axis = convert_uint8_to_bytes(y_axis)
    x_moment = b'\x01' if x_moment else b'\x00'
    y_moment = b'\x01' if y_moment else b'\x00'
    data = [b'\x0e',b'\x04',x_axis,y_axis,x_moment,y_moment]
    for i in data:
        ports.ser.write(i)

@wrong
@start
@stop
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
        ports.ser.write(i)

@wrong
@start
@stop
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
        ports.ser.write(i)

@wrong
@start
@stop
def steering_angle(main_panel:int, gesture:int, source:int, hot:int):
    main_panel = 0 if main_panel<0 else main_panel%8
    gesture = 0 if gesture<0 else gesture%8
    source = 0 if source<0 else source%8
    hot = 0 if hot<0 else hot%8
    main_panel = convert_uint8_to_bytes(main_panel)
    gesture = convert_uint8_to_bytes(gesture)
    source = convert_uint8_to_bytes(source)
    hot = convert_uint8_to_bytes(hot)
    data = [b'\x14',b'\x04',main_panel,gesture,source,hot]
    for i in data:
        ports.ser.write(i)


@wrong
@start
@stop  # 未完成代码，不要使用
def communicate(content:str):
    pass
