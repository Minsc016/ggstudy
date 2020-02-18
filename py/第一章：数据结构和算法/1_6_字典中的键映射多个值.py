#########################################################################
# File Name: 1_6_字典中的键映射多个值.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Oct 23 11:34:26 2019
#########################################################################
#!/usr/bin/env python3

# 一个字典 中 一个键对应一个值，
#或者：
d = {
        'a':[1,2,3],
        'b':[4,5]
        }

e = {
        'a':{1,2,3},
        'b':{4,5}
        }

# 保持 插入顺序就使用 List ， 去掉 重复元素  就使用 集合。

# collections 中 的 dufaultdict 模块 构建 这样的字典，自动初始化，只需关注添加元素操作。
from collections import defaultdict as dd

d1 = dd(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)

e1 = dd(set)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)

print(d,d1)
print(e,e1)
# NOTICE:defaultdict 会自动为将要访问的键创建 映射实体， 如果并不需要这种特性，可以在普通字典上用 setdefault()方法来代替。eg:
d = {} # A　regular dictionary
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)

# 自己 实现 多值映射字典
pairs = [('a',1),('a',2),('b',4),('b',5)]
d = {}
for key,value in pairs:
    if key not in d:
        d[key] = []
        d[key].append(value)
print(d)

# 使用defaultdict
d = dd(list)
for key,value in pairs:
    d[key].append(value)

print(d)
