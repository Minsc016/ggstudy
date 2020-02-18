#########################################################################
# File Name: 1_16_过滤序列元素.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 24 19:40:48 2019
#########################################################################
#!/usr/bin/env python3

# 你有一个数据序列， 想 利用 一些规则 从中 提取出来 需要的值 或者 缩短序列
mylist = [ 1,4,-5,10,-7,2,3,-1]
# 最简单的过滤序列元素方法： 列表推导
print([n for n in mylist if n>0])

print([n for n in mylist if n<0])

# 使用 列表推导 的 一个潜在缺陷： 如果输入非常大，会产生非常大的结果集，占用大量内存。
# 使用 生成器 表达式 迭代产生过滤的元素
pos = (n for n in mylist if n > 0)
print(type(pos))
for n in pos:
    print(n,end=' ')
print()

# 比较 复杂 的 过滤规则
values = [ '1','2','-3','-','4','N/A','5' ]
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int,values))
print(ivals)
# 
# filter() 函数 创建一个 迭代器， 要用List 去转换成列表。
# 列表推导 和 生成器 通常情况下 是 过滤数据最简单的方式。 过滤同时 还可以 转换数据：
import math
print([ math.sqrt(n) for n in mylist if n > 0])

# 将不符合条件的用新值代替，比如：
clip_neg = [ n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [ n if n < 0 else 0 for n in mylist]
print(clip_pos)

# 一个 过滤工具：：：：itertools.compress()
# 输入一个 iterable对象和一个对应的Boolean选择器，输出iterable对象中对应选择器为True的对象.
# 当使用一个 相关联 的序列 来 过滤某个序列的时候，非常有用：
addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4081 W BROADWAY',
        '1030 W GRANVILLE',
        ]
counts = [0,3,10,4,1,7,6,1]
# 输出对应count值大于5的地址
from itertools import compress
more5 = [ n > 5 for n in counts]
print(more5)
print(list(compress(addresses,more5)))
