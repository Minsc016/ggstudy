#########################################################################
# File Name: 4_2_代理迭代.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 24 16:17:44 2019
#########################################################################
#!/usr/bin/env python3

# 构建　了　一个　自定义容量对象，里面包含列表，元组，或其他可迭代对象，
# 目的： 直接在这个新容器对象上执行迭代操作。

# 解决方案
# 实际上 只需要定义一个 __iter__()方法，将迭代操作代理到容器内部的对象上去。比如：
class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node{!r}'.format(self._value)

    def add_child(self,node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    #Ｏｕｔｐｕｔｓ　Ｎｏｄｅ（１），Ｎｏｄｅ（２）
    for ch in root:
        print(ch)
    

# __iter__() 方法 简单的 将 迭代请求传递给 内部的 _children 属性

# Python的迭代器协议需要 __iter__() 方法 返回了一个实现了 _next__() 方法的迭代器对象。
# 如果只是迭代遍历其他容器的内容，无需担心底层实现。
# 只需要做 传递迭代请求 即可

# 这里的 iter() 函数的使用简化了代码， iter(s) 只是简单的通过调用
# __iter__() 方法来返回对应的迭代器对象，
# 就跟len(s)会调用s.__len__() 原理是一样的。
