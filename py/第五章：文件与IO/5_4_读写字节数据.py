#########################################################################
# File Name: 5_4_读写字节数据.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Jan 17 11:03:45 2020
#########################################################################
#!/usr/bin/env python3

# 读写二进制文件，比如图片，声音文件等。
# 使用模式为rb 或 wb 的open() 函数来读取或写入二进制数据。
# Read the entire file as a sinle byte string
with open('somefile.bin','rb') as f:
    data = f.read()

# Write binary data to a file
with open('somefile.bin','wb') as f:
    f.write(b'Hey nigga') 

# 在读取 二进制数据 时， 需要指明 所有返回的数据都是字节字符串格式的，
# 而不是文本字符串。
# 类似，写入时 必须保证参数是字节形式 对外 暴露数据的对象（比如字节字符串，字节数组对象等）。

# 在 读取二进制 数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱。
# 索引和迭代动作返回的是字节的值 而不是字节字符串。
# Text string
t = 'Hello Motherfucker'
print(t[0])
for c in t:
    print(c)

# Byte string
b = b'Hello World'
print(b[0])
for c in b:
    print(c)


# 从二进制模式的文件中读取或写入文本数据，必须确保进行解码和编码操作。
with open('somefile.bin','rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin','wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

# 二进制I/O 还有一个鲜为人知 的特性就是数组和C结构体类型能直接被写入，
# 而不需要中间转换为自己对象。
import sys
nums = array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
    f.write(nums)

# 这个使用与任何实现了 被称之为 "缓冲接口" 的对象，这种对象会直接暴露其底层的
# 内存缓冲区 能处理它的操作。
# 二进制数据的写入就是这类操作之一。

# 很多对象还允许通过使用文件对象的 readinto() 方法直接读取二进制数据到
# 其底层的内存中去，
import array
a = array.array('1',[0,0,0,0,0,0,0,0])
with open('data.bin','rb') as f:
    f.readinto(a)

print(a)

# 但是使用这种技术的时候需要格外小心，因此它通常具有平台相关性。
# 并且依赖字长和字节顺序（高位优先和低位优先）。-->5_9
