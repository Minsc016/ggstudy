#########################################################################
# File Name: 1_18_映射名称到序列元素.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Oct 28 11:26:52 2019
#########################################################################
#!/usr/bin/env python3

# 下标访问 ==> 名称访问

# collections.nametuple() 函数
# 一个返回Python 中标准元组类型子类的一个工厂方法
# 传递一个类型名，和需要的字段；返回一个类。
from collections import namedtuple
Subscriber = namedtuple('Subsciber',['addr','joined'])
sub = Subscriber('jonesy@example.com','2012-10-19')
print(sub,sub.addr,sub.joined)

# namedtuple 类实例 可以 跟 元组类型 交换。 支持所有普通元组操作，比如索引和解压
len(sub)
addr,joined = sub
print(addr,joined)

# 命名元组 的 一个主要用途 是把代码 从 下标操作中解放出来

# 对比：
# 下标操作：
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# 命名元组操作：
from collections import namedtuple
Stock = namedtuple('Stock',['name','shares','price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# 命名元组的另一个用途： 替代字典
# 字典 存储 需要更多的内从空间，如果要构建一个非常大的包含字典的数据结构，
# 使用元组会更加高效；    但是：：：：命名元组不可更改。

s = Stock('ACME',100,123.45)
print(s)
try:
    s.shares = 75
except AttributeError as AE:
    print(AE)

# 改变命名元组 属性的值，使用 _replace()方法。
# eg:
s = s._replace(shares=75)
print(s)

from collections import namedtuple
Stock = namedtuple('Stock',['name','shares','price','date','time'])
# Cteate a prototype instance
stock_prototype = Stock('',0,0.0,None,None)
print(stock_prototype)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name':'ACME','shares':100,'price':123.45}
print(dict_to_stock(a))

b = {'name':'ACME','shares':75,'price':123.45,'date':'12/17/2012'}
print(dict_to_stock(b))

# 如果 需要 定义 一个 更新 很多 实例属性 的高效数据结构，命名元组并不合适。
# 这时候应该考虑 一个 ___slots__方法的类
