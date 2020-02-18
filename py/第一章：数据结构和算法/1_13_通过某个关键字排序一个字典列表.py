#########################################################################
# File Name: 1_13_通过某个关键字排序一个字典列表.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 24 10:20:59 2019
#########################################################################
#!/usr/bin/env python3

# 根据 某个 或 某几个 字典字段 来排序 这个 字典列表

# operator 模块 的 itemgetter 函数
print('{:-^60}'.format('rows'))
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': '1003'},
{'fname': 'David', 'lname': 'Beazley', 'uid': '1002'},
{'fname': 'Johj', 'lname': 'Cleese', 'uid': '1001'},
{'fname': 'Big', 'lname':'Jones', 'uid': '1004'}
]
for row in rows:
    print(row)
print('{:-^60}'.format('rows_by_fname'))
from operator import itemgetter
rows_by_fname = sorted(rows,key = itemgetter('fname'))
rows_by_uid = sorted(rows,key = itemgetter('uid'))
for row in rows_by_fname:
    print(row)
print('{:-^60}'.format('rows_by_uid'))
for row in rows_by_uid:
    print(row)

# itemgetter() 函数 也支持多个keys ,比如 下面代码：
rows_by_lfname = sorted(rows,key = itemgetter('lname','fname'))
print('{:-^60}'.format('rows_by_lfname'))
for row in rows_by_lfname:
    print(row)

# rows 被传递到接受一个关键字参数的sorted() 内置函数。
# 这个参数 是 hasbable 类型，并且从 rows 接受一个单一元素，然后返回被用来排序的值
# itemgetter()函数 创建 此 hashable 对象
# operator.itemgetter() 函数有一个被  rows 中的记录用来 查找值的索引参数 。
# 传入多个索引参数给 itemgetter 返回一个包含所有元素值的元组callable对象

# itemgetter 比 lambda r:r['key'] 快一点
# 同样适用于 min()、max()函数
