#########################################################################
# File Name: 4_9_排列组合的迭代.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Dec 26 14:29:56 2019
#########################################################################
#!/usr/bin/env python3


# 迭代遍历一个集合中 元素的所有可能的排列或 组合
# 解决方案；
# itertools 模块 提供了三个函数来解决这类问题。
# 其中一个是 itertools permutations() ，它接受一个集合并产生一个元组序列，
# 每个元组由集合中所有元素的一个可能排列组成。
# 即 通过打乱集合中元素排列顺序生成一个元组。
items = ['a','b','c']
from itertools import permutations
for p in permutations(items):
    print(p)
# 得到指定长度的所有排列，传递一个可选的长度参数
for p in permutations(items,2):
    print(p)

# 使用 itertools.combinations() 可得到输入集合中元素的所有的组合，比如
from itertools import combinations
for c in combinations(items,3):
    print(c)

for c in combinations(items,2):
    print(c)
for c in combinations(items,1):
    print(c)

# 对于combinations()来讲，元素的顺序已经不重要了。即，组合（'a','b')跟（'b','a')其实是一样的。
# 在计算组合的时候，一旦元素被选取就会从候选中删除掉；
# 而函数itertools.combinations_with_replacement()允许一个元素被选择多次。
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items,3):
    print(c)

# itertools 的一部分功能。
# 自己手动实现排列组合算法，花点脑力。
# 有些复杂的迭代问题，最好可以看看itertools模块。

