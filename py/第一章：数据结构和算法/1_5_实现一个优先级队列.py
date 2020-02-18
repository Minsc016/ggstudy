#########################################################################
# File Name: 1_5_实现一个优先级队列.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Oct 23 10:45:00 2019
#########################################################################
#!/usr/bin/env python3

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)

print(q.pop(),q.pop(),q.pop(),q.pop())

# heapq 的heapq.heappush() 和 heappop() 分别在　队列 _queue 上插入 和删除第一个元素。并且队列 _queue 保证第一个元素拥有最高优先级。 
# index 可以保证同等优先级 元素的正确顺序（插入的顺序)。
# 使用了3个元素的元组， 优先级，Index，和item本身。

