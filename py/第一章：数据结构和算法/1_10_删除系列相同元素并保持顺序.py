#########################################################################
# File Name: 1_10_删除系列相同元素并保持顺序.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Oct 23 17:13:26 2019
#########################################################################
#!/usr/bin/env python3

# 保持顺序： 使用 生成器
# 消除重复： 使用集合set()

# Hashable 元素的方法：
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))

# 对不可哈希类型，比如dict，改：
def dedupe(items,key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
# key参数 指定一个函数，将 序列元素 转换为hashable 类型
a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
print(list(dedupe(a,key = lambda d:(d['x'],d['y']))))

# 如果只想消除重复，可以构造集合:
# set(a)

# 读取一个文件，消除重复行：
# with open(somefile,'r') as f:
#     for line in dedupe(f):
#         .......
