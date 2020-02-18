#########################################################################
# File Name: 4_8_跳过可迭代对象的开始部分.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Dec 26 11:33:29 2019
#########################################################################
#!/usr/bin/env python3

# 遍历一个可迭代对象，但是它开始的某些元素并不需要，跳过。

# itertools 模块 中 有一些 函数可以完成这个任务，首先介绍的是itertools.dropwhile() 函数
# 使用方法： 传递一个 函数对象 和 一个可迭代对象，返回一个迭代器对象，
# 丢弃原有序列中知道函数返回Flase 之前的元素，然后返回后面所有元素。
# 假定读取一个开始部分是几行注释的文件。

#with open('./4_8_跳过可迭代对象的开始部分.py') as f:
#    for line in f:
#        print(line,end='')
#
#print('\n\n\n')
## 跳过开始注释行：：：：
#from itertools import dropwhile
#with open('./4_8_跳过可迭代对象的开始部分.py') as f:
#    for line in dropwhile(lambda line:line.startswith('#'),f):
#        print(line,end='')
#
#
## 例子基于 根据 某个 测试函数 绕过开始的元素，如果已经明确知道跳过的元素个数的话，
## 可以使用 itertools.islice() 来代替，比如：
#from itertools import islice
#items = ['a','b','c',1,4,10,15]
#for x in islice(items,3,None):
#    print(x)
#
# islice() 函数最后的None函数指定了获取 从第3个到最后的所有元素。
# 如果None 和 3的位置对调，意思就是获取前三个元素。跟切片操作一样的。[3:]、[:3]

# 函数dropwhile() 和 islice() 起始是两个帮助函数，为了避免冗余代码like this:
#with open('./4_8_跳过可迭代对象的开始部分.py') as f:
#    # Skip over initial comments
#    while True:
#        line = next(f,'')
#        if not line.startswith('#'):
#            break
#
#    # Process remaining line
#    while line:
#        # Replace with useful processing
#        print(line,end='')
#        line = next(f,None)
#
# 跳过一个可迭代对象的开始部分跟通常的过滤是不同的，比如上述代码的第一部分重写：
with open('./4_8_跳过可迭代对象的开始部分.py') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line,end='')


# 这样写可以跳过开始部分的注释行，也会跳过文件中其他所有注释行。
# 适用于所有可迭代对象，包括事先不能确定大小的，比如生成器，文件及其类似的对象。
