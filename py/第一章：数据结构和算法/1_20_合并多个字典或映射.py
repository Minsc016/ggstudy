#########################################################################
# File Name: 1_20_合并多个字典或映射.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Nov  1 14:58:43 2019
#########################################################################
#!/usr/bin/env python3

# 有多个字典或者 映射，  从 逻辑上  合并 为 一个单一的映射 后 执行 某些操作，
# 比如查找值 或者 检查某些键 是否存在 

# 假如现在有两个字典：
a = {'x':1,'z':3}
b = {'y':2,'z':4}
# 假设必须在 两个字典 中 执行 查找操作（比如 先从a 中找，找不到再在b中找）.
# 解决方案 使用 collections 中的 ChainMap 类
from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1(from a)
print(c['y']) # Outputs 2(from b)
print(c['z']) # Outputs 3(from a)

# 一个ChainMap 接受多个字典并将它们在 逻辑上 变为一个字典
# 并非 真的合并， 只是在内部 创建 一个容纳这些字典的列表 并重新定义了常见的字典操作来遍历列表
print(len(c))
print(list(c.keys()))
print(list(c.values()))
# 如果出现重复键，第一次出现的映射值将会返回。因此，例子程序中的c['z']总是会返回字典a中对应的值，而不是b中对应的值。

# 字典的更新 或 删除 操作总是影响的是列表的第一个字典，比如：
c['z'] = 10
print(a,b,c)
c['w'] = 40
print(a,b,c)
del c['x']
print(a,b,c)
try:
    del c['y']
except KeyError as ke:
    print(ke,'shows that update/del only worked for the first dict in Ｃｈａｉｎ')


# ChainMap 对于 编程语言中的 作用范围变量（比如globals,locals等）是非常有用的。
# 事实上，有一些方法可以使它变得简单：

values = ChainMap()
values['x'] = 1
# add a new mapping
values = values.new_child()
values['x'] =2
# add a new mapping
values = values.new_child()
values ['x'] =3
print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values['x'])
print(values)

# 作为ChainMap的替代，你可能会考虑使用Update（）方法将两个字典合并。
# 比如:
a = {'x':1,'z':3}
b = {'y':2,'z':4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

# also worked. 但是它需要你创建一个 完全不同的字典对象（或者破坏现有字典结构），
# 同时，如果原字典更新，不会反应到合并字典中。
a['x'] = 13
print(merged['x'])

# ChainMap 使用原来的字典，不会创建新字典。
a = {'x':1,'z':3}
b = {'y':2,'z':4}
merged = ChainMap(a,b)
print(merged['x'])
a['x'] = 666
print(merged['x'])
