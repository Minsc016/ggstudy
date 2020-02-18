#########################################################################
# File Name: 4_5_反向迭代.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Dec 25 10:16:05 2019
#########################################################################
#!/usr/bin/env python3

# 反方向迭代一个序列。

# 1.使用内置的reversed() 函数，eg：
a = [1,2,3,4]
for x in reversed(a):
    print(x)

# 反向迭代仅仅当对象的大小可预先确定 或者 对象实现了__reversed__()的特殊方法时才能生效。
# 如果两者都不符合，那你必须先将对象转换为一个列表才行，比如：
# print a file backwards
f = open('./4_5_somefile')
for line in reversed(list(f)):
    print(line,end='')
f.close()

# 注意如果 可迭代对象元素很多的话， 将其 预先转换为一个列表要消耗大量的内存。


# 通过自定义类上 实现 __reversed__()方法 来实现反向迭代，eg：
class Countdown:
    def __init__(self,start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n<=self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)

for rr in Countdown(30):
    print(rr)

# 定义一个 反向迭代器 可以使得代码非常高效
# 不需要将数据填充到列表中 再反向迭代。
