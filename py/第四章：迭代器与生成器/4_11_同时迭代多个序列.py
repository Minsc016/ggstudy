#########################################################################
# File Name: 4_11_同时迭代多个序列.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Dec 30 10:14:38 2019
#########################################################################
#!/usr/bin/env python3

# 同时迭代多个序列，每次分别从一个序列中取一个元素
# 解决方案：
# zip() 函数

xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,62,99]
for x,y in zip(xpts,ypts):
    print(x,y)


# zip(a,b) 会生成一个 可返回元组（x,y) 的迭代器，其中x来自a，y来自b。
# 迭代长度 跟 参数中 最短序列 一致。

a = [1,2,3]
b = ['q','w','e','r','t']

for i in zip(a,b):
    print(i)


# itertools.zip_longest() 来代替效果：
from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

for i in zip_longest(a,b,fillvalue = 0):
    print(i)


# zip() 处理数据，比如一个 头列表 一个 值列表：
headers = ['name','shares','price']
values = ['ACME',100,490.1]
# 使用zip打包，并生成一个字典
s = dict(zip(headers,values))
print(s)

# 或者输出：
for name,val in zip(headers,values):
    print(name,'=',val)

#
# zip() 可以接受多余两个序列的参数，生成的结果元组中元素个数 跟 输入序列个数一样。
a = [1,2,3]
b = ['a','b','c']
c = ['x','y','z']

for i in zip(a,b,c):
    print(i)

# 强调： zip() 函数会创建一个迭代器作为结果返回。
# 如果需要将结果的值存储在列表中，要使用list() 函数，
print(zip(a,b))
print(list(zip(a,b)))
