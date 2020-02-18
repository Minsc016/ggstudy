#########################################################################
# File Name: 4_12_不同集合上元素的迭代.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Dec 30 10:30:56 2019
#########################################################################
#!/usr/bin/env python3

# 想在多个对象执行相同的操作，但是这些对象在不同的容器中，
# 希望代码在不失可读性的情况下避免写重复的循环。

# itertools.chain() 方法可以 用来简化此任务。
# 接受一个可迭代对象列表作为输入，并返回一个迭代器。
# 有效的屏蔽掉在多个容器中迭代细节，eg:
from itertools import chain
a = [1,2,3,4]
b = ['x','y','z']
for x in chain(a,b):
    print(x)

# 使用chain() 的一个常见场景是当你想对不同的集合中所有元素执行某些操作的时候，比如：
# Various working sets of items
active_items = set()
inactive_items = set()

# Iterate over all items
for item in chain(active_items,inactive_items):
    #Process item
    pass

# 这种解决方案要比下面的方式（使用两个单独的循环） 更加优雅：
for items in active_items:
    #Process item
    pass
for item in inactive_items:
    #process item
    pass


# 第一种方案中，a+b 操作会创建一个全新的序列并要求 a 和 b 的类型一致，
# chain() 不会有这一步，所有如果输入序列非常大的时候会很省内存。
# 并且当可迭代对象类型不一样的时候chain() 同样可以很好的工作。
