#########################################################################
# File Name: 1_9_查找两字典的相同点.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Oct 23 16:57:35 2019
#########################################################################
#!/usr/bin/env python3

# 怎样在两个字典中 查找相同点 比如相同的键 相同的值 等等

a = {
        'x':1,
        'y':2,
        'z':3
        }
b = {
        'w':10,
        'x':11,
        'y':2
        }

# find keys in common
print(a.keys() & b.keys() )# {'x','y'}
# Find keys in a that are not in b
print(a.keys() - b.keys() )#{'z'}
# Find (key,value) pairs in common
print(a.items() & b.items())

# 用于修改 或者 过滤元素
# eg:以 现有字典 构造 一个 排除 几个 指定键 的 新字典， ：：：：
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z','w'}}
# c is {'x':1,'y':2}
print(c)
# keys() 键视图 对象 也支持 集合操作::::并、交、差
# items()
# values() 不支持 集合操作。 值视图不能保证所有值互不相同。==>set(values())


