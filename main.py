from ports import *
print('aa55000100000a0d'.encode('utf-8'))
print(('0xaa55000100000a0d'.encode('utf-8').hex()))
print(('aa55000100000a0d'.encode('utf-8').hex()))
print(('0xa'.encode('utf-8').hex()))
print(('a'.encode('utf-8').hex()))
print(b'aa55000100000a0d')
print(type(b'\xaa'.hex()))
print(b'\xaa')
print(b'aa')
print(type(b'\xaa'))
print(type(b'hello'))
print(b'hello')

print((b'\xaa55000100000a0d'.hex()))
print((b'aa55000100000a0d'.hex()))

num = '{:x}'.format(100)
print(num.encode('utf-8'))
print(num.encode('utf-8').hex())
sd = convert_float32_to_bytes(123.12)
print('sd: ',sd,type(sd),sd.hex(),str(sd.hex()))
print(convert_bytes_to_string(sd))
print(convert_string_to_bytes('1234'))




