#########################################################################
# File Name: 3_5_字节到大整数的打包与解包.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Dec 12 20:46:19 2019
#########################################################################
#!/usr/bin/env python3

# 一个字节字符串 将其解压成一个整数
# 或者 一个大整数 转换为一个字节字符串

# 方案
# 假设需要处理一个拥有 128位 长的16个元素的字节字符串，比如：
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

# 为了将bytes 解析成整数，使用int.from_bytes() 方法，并制定字节顺序：
print(data)
print(len(data))
print(int.from_bytes(data,'little'))
print(int.from_bytes(data,'big'))

# 将 一个大整数转换为一个字节字符串，使用 int.to_bytes() 方法，并像下面这样指定字节数和字节顺序。
x = 94522842520747284487117727783387188
print(x.to_bytes(16,'big'))
print(x.to_bytes(16,'little'))

# 密码学/网络可能会用到。eg.IPv6 网络地址，128位的整数。
# --》6_11struct 模块 解压字节。 struct 对整数大小有限制。
# 解压多个字节串 并将结果合并为最终结果：：：：：：：：：：：：：：：P::

print(data)
import struct
hi,lo = struct.unpack('>QQ',data) #????????????????????
print((hi<<64) + lo)

# 字节顺序规则（little 或 big）仅 指定了 构建整数时的字节的低位高位 排列方式，
x = 0x01020304
print(x)
print(x.to_bytes(4,'big'))
print(x.to_bytes(4,'little'))

# 不适合 将 整数 打包为 字节字符串。
# 可以使用 int.bit_length() 方法来决定需要多少字节位 来存储这个值。

x = 523**23
print(x)
try:
    x.to_bytes(16,'little')
except OverflowError as oe:
    print(oe)

print(x.bit_length())
nbytes,rem = divmod(x.bit_length(),8)
if rem:
    nbytes += 1

print(x.to_bytes(nbytes,'little'))
