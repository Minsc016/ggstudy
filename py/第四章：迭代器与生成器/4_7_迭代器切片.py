#########################################################################
# File Name: 4_7_迭代器切片.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Dec 26 11:19:27 2019
#########################################################################
#!/usr/bin/env python3


# 想 得到 一个 由 迭代器 生成 的 切片对象， 但是标准切片操作并不能做到。

# 解决方案：
# 函数 itertools.islice() 正好适用 迭代器和生成器上做切片操作。
def count(n):
    while True:
        yield n
        n += 1

c = count(0)
try:
    c[10:20]
except TypeError as te:
    print(te)

# now using islice()
from itertools import islice
for x in islice(c,10,20):
    print(x)

# 迭代器 和 生成器不能使用 标准的切片操作。 因为长度事先不知道（也没有实现索引）。
# 函数islice() 返回一个可以生成指定元素的迭代器。

# 通过遍历并丢弃知道切片开始索引位置的所有元素，然后一个个返回元素，直到切片结束索引位置。

# islice() 会消耗掉传入的迭代器中的数据。
#### 必须考虑迭代器是不可逆的事实 ####
# 如果需要之后再次访问迭代器，就得将它的数据放入列表中。
