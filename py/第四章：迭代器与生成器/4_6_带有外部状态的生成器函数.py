#########################################################################
# File Name: 4_6_带有外部状态的生成器函数.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Dec 26 09:54:22 2019
#########################################################################
#!/usr/bin/env python3

# 定义一个生成器函数， 用它调用某个 需要暴露给用户使用的外部状态值。
# 解决方案：
# 1.如果想让生成器暴露外部状态给用户，可以简单的将它实现为一个类，
# 然后把生成器函数放到 __iter__() 方法中过去。

from collections import deque

class linehistory:
    def __init__(self,lines,histlen=3):
        self.lines = lines
        self.history = deque(maxlen = histlen)

    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append((lineno,line))
            yield line

    def clear(self):
        self.history.clear()


# 使用这个类，当做是一个普通的生成器函数。
# 由于可以创建一个实例对象，于是可以访问内部属性值。
# 比如history 属性 或者 claer() 方法。
with open('4_6_somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno,hline in lines.history:
                print('{}:{}'.format(lineno,hline),end='')

# 关于生成器，很容易 掉进函数无所不能的陷阱。
# 如果 生成器函数需要跟你的程序 其他部分打交道的话（比如暴露属性值，允许通过方法调用来控制等）
# 可能会导致代码复杂。

# 使用上面的 定义类 的方法，在__iter__()方法中定义生成器 不会改变任何算法及逻辑。
# 由于它是类的一部分，所以允许定义各种属性和方法来供用户使用。
# 如果在迭代操作时不适用 for循环语句，那么需要先调用iter()函数。

f = open('./4_6_somefile.txt')
lines = linehistory(f)
try:
    next(lines)
except TypeError as te:
    print(te)

# Call iter() first,then start iterating
it = iter(lines)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
