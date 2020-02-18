#########################################################################
# File Name: 4_16_迭代器代替while无限循环.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Jan 16 17:03:15 2020
#########################################################################
#!/usr/bin/env python3

# while 循环迭代处理数据，
# 需要调用某个函数或者和一般迭代模式不同的测试条件。
# 用迭代器重写。

# 一个常见的IO操作程序：
CHUNKSIZE=8912
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

# 用 iter() 代替

def reader2(s):
    for chunk in iter(lambda :s.recv(CHUNKSIZE),b''):
        pass
        #process_data(data)

# 试验 例子:
import sys
f = open('/etc/hosts')
for chunk in iter(lambda: f.read(10),''):
    n = sys.stdout.write(chunk)

# iter函数 一个鲜为人知的特性： 它接受一个可选的callable 对象 和
# 一个标记（结尾） 值作为输入参数。
# 当以 这种方式使用的时候，它会创建一个迭代器，这个迭代器会不断调用callable 对象直到 
# 返回值 和标记值相等为止。

# 这种特性的方法对于一些 特定的会被重复调用的函数很有效果，比如涉及到
# I/O调用的函数。
# 举例来讲，如果你想从套接字或 文件中 以 数据块的方式读取数据
# 通常要不断重复的执行 read() recv()
# 并在后面紧跟一个文件结尾测试来决定是否终止。
# iter() 调用可以将两者结合起来，其中 lambda 函数参数是为了创建一个无参的
# callable 对象，并为recv或read() 方法提供了size参数。
