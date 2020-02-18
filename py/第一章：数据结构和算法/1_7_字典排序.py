#########################################################################
# File Name: 1_7_字典排序.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Oct 23 15:27:12 2019
#########################################################################
#!/usr/bin/env python3

# 使用 collections 中的 OrderedDict类， 控制 一个字典中元素的顺序。

from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs 'foo 1','bar 2','spam 3','grok 4'

# for key in d:
#     print(key,d[key])
for key,value in d.items():
    print(key,':',value)

#　当想要构建一个将来需要序列化或 编码成其他格式的 映射 的时候，OrderedDict是非常有用的。
# 比如，精确控制 以 JSON 编码后 字段 的顺序，可以先用 OrderedDict 来构建这样的数据：
import json
josn.dumps(d)

# OrderedDict 内部维护着 一个 根据键 插入顺序 排序的双向链表，
# 每次当一个新的元素插入进来的时候，它 会 被放到链表 的尾部。
# 对于一个已经存在的键的重复赋值 不会 改变键的顺序。
# ＮＯＴＩＣＥ：一个OrderedDict的大小是普通字典的两倍，因为它内部维护着另外一个链表。
# 所以 构建 一个大量 OrderedDIct实例的时候，需要 权衡 OrderedDIct的作用是否打过额外内存消耗的影响。
# 


