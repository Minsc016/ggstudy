#########################################################################
# File Name: 5_6_字符串的IO操作.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: 2020年02月20日 星期四 10时27分51秒
#########################################################################
#!/usr/bin/env python3


# 使用 操作文件对象的程序来操作文本或者二进制字符串

# 解决方案：
# 使用io.StringIO() 或者 io.BytesIO() 类 来创建 类文件对象 操作字符串数据。
import io

s = io.StringIO()
s.write('Hello World!\n')
print('This is a test',file=s)

# Get all of the data written so far
print(s.getvalue())


# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))

print(s.read())

#io.StringIO() 只能用于文本，如果要操作二进制数据，要使用io.BytesIO类来代替。
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())

# 想 模拟一个普通文件 的时候StringIO和BytesIO 类是非常有用的。
# 在单元测试中，使用StringIO 来创建一个包含测试数据的类文件对象。
# 此对象可以传给 某个参数为普通文件对象的函数。
# StringIO 和 BytesIO 实例 没有正确的整数类型的文件描述符。
# 因此，它们不能在那些需要使用真实的系统级文件如 文件、管道、套接字 的程序中使用。
