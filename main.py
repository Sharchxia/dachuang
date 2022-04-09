from ports import port_init,tx,rx
import time

# print(port_init.port_list())
print(port_init.port_set('COM3'))

tx.open_all()  # 开启所用端口及功能,每次卫星开机执行一次，保证不会出问题
time.sleep(1)  # 每个写操作后面都应有，秒数自定

tx.wheel_speed_control(20)
time.sleep(3)

print('angle_euler:',rx.angle_euler())
print('angle_speed:',rx.angle_speed())
print('angle_acc:',rx.angle_acc())
print('light:',rx.light_status())
print('source:',rx.source_storage())
print('temper:',rx.temper_status())
