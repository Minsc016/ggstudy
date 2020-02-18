#########################################################################
# File Name: 2_20_字节字符串上的字符串操作.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 10 10:15:50 2019
#########################################################################
#!/usr/bin/env python3

# 字节字符串 同样支持 部分和 文本字符串 一样的内置操作：：：：
data = b'Hello World'
print(data[0:6])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'World',b'Cruel World'))

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello',b'Hello World'))

# 可以使用正则表达式 匹配字节字符串----正则表达式本身必须是字节串。
data = b'FOO:BAR,SPAM'
import re
try:
    print(re.split('[:,]',data))
except TypeError as te:
    print(te)
print(re.split(b'[:,]',data))

# 大多数 文本字符串上的操作 可 用于 字节字符串，但是
# 不同点： 1.字节字符串 索引操作返回整数 而不是单独字符：：：：
a = 'Hello World' #Text String
print(a[0],a[1],a[2],sep='\t')
b = b'Hello World' #byte String
print(b[0],b[1],b[2],sep='\t')

# 2.字节字符串 不会提供一个美观的字符串表示，
# 也不能很好的打印出来，
# 除非先解码为一个文本字符串。

s = b'Hello World'
print(s,s.decode('ascii'),sep='\t')

# 3.不存在 适用于 字节字符串 的 格式化操作
try:
    print(b'%10s %10d %10.2f' % (b'ACME',100,400.1)) # 跟教材不符，这里没有报错。
    print(b'{} {} {}'.format(b'ACME',100,400.1))
except AttributeError as ae:
    print(ae)

# 如果要 格式化 字节字符串，先使用标准文本字符串，然后将其编码为字节字符串。
print('{:>10s} {:>10d} {:>10.2f}'.format('ACME',100,200.3).encode('ascii'))


# 使用字节字符串 可能会改变一些操作的语义，特别是那些跟文本系统有关的操作。
# 比如----使用一个 编码为字节的 文件名，而不是一个普通的文本字符串，会禁用文件名的编码/解码。
#　write a UTF-8 filename
with open('jalap\xf1o.txt','w') as f:
    f.write('spicy')

# get a directory
import os
print(os.listdir('.')) # Text string(names are decoded)
print(os.listdir(b'.')) # Byte string(names left as bytes)

# NOTICE: 给目录名传递一个字节字符串----结果中文件名 未解码 。
