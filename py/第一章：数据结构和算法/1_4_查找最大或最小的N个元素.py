#########################################################################
# File Name: 1_4_查找最大或最小的N个元素.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Oct 22 09:16:18 2019
#########################################################################
#!/usr/bin/env python3

# heapq 模块的函数: nlargest，和nsmallest
from heapq import nlargest as nl
from heapq import nsmallest as ns

nums = [1,8,2,23,7,-4,18,42,37,2]
print(nl(3,nums))
print(ns(3,nums))

#ks=['name','shares','price']
#portfolio=[{},{},{},{},{},{}]
#for i in range(6):
#    for k in ks:
#        portfolio[i][k]=input()
#
#print(portfolio)
#
portfolio = [{'name': 'IBM', 'shares': '100', 'price': 91.1}, {'name': 'AAPL', 'shares': '50', 'price':543.22}, {'name': 'FB', 'shares': '200', 'price': 21.09}, {'name': 'HPQ', 'shares': '35','price': 31.75}, {'name': 'YHOO', 'shares': '45', 'price': 16.35}, {'name': 'ACME', 'shares': '75', 'price': 115.65}]

cheap = ns(3,portfolio,key = lambda d:d['price'])
expensive = nl(3,portfolio,key= lambda d:d['price'])

print("cheapest 3: ",cheap,"\n","expensivest 3: ",expensive)

# 集合中
heap = list(nums)
import heapq
heapq.heapify(heap)
print(heap)
# 堆 数据结构 最重要的 特征 是heap[0] 永远是 最小 的元素。
# 并且剩余的元素可以很容易的通过调用heapq.heappop()方法得到。
# 该方法会先将第一个元素弹出来，然后用下一个最小的元素取代被弹出元素
# （时间复杂度 为 O(log N)，N是堆大小。
print(heapq.heappop(heap),heapq.heappop(heap),heapq.heappop(heap))
# 当要查找的元素个数相对比较小的时候，函数nlargest和nsmallest是很合适的
# 如果仅要查找唯一的最小/大(N=1)的元素的话，使用min()和max()函数会更快。
# 如果N的大小和集合大小接近的时候，通常先排序这个集合然后使用切片操作会更快。、
# sorted(items)[:N]或者sorted(items)[-N:]

