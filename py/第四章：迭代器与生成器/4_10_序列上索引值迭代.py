#########################################################################
# File Name: 4_10_序列上索引值迭代.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Dec 26 14:51:16 2019
#########################################################################
#!/usr/bin/env python3

# 在迭代一个序列的同时 跟踪正在被处理 的 元素索引。
# 解决方案，内置的 enumerate() 函数。
my_list = ['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)

# 行号从1 开始，传递一个开始参数。
for idx,val in enumerate(my_list,1):
    print('{}:{}'.format(idx,val))

# 在遍历文件时想在错误消息中使用行号定位时非常有用：
def parse_data(filename):
    with open(filename,'rt') as f:
        for lineno,line in enumerate(f,1):
            fields = line.split()
            try:
                count = int(fields[1])
                pass
            except ValueError as ve:
                print('Line {}:Parse Error:{}'.format(lineno,ve))

# enumerate() 对于跟踪 某些值 在列表中出现的位置 是很有用的。
# 所以如果要将一个文件中 出现的单词 映射到它出现的行号上去，可以很容易的利用enumerate()：
from collections import defaultdict
word_summary = defaultdict(list)
with open('./4_10_myfile.txt','r') as f:
    lines = f.readlines()

for idx,line in enumerate(lines,1):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

# 处理完文件后打印word_summary，它是一个字典（defaultdict），对于每个单词有一个key
# 每个key 对应的值是一个由这个单词出现的行号组成的列表，可作为文本的简单统计。

# 当你想 额外定义 一个计数变量的时候，使用enumerate() 函数。
# 不用enumerate:
f = open('./4_10_myfile.txt','r')
lineno = 1
for line in f:
    # Process 
    pass
    lineno += 1

# 使用enumerate:
for lineno,line in enumerate(f):
    #Process
    pass
f.close()

# enumerate() 函数返回 的 是一个 enumerate对象实例，它是一个迭代器，
# 返回连续的包含一个计数 和 一个值的元组
# 元组中的值通过在传入序列上调用next()返回。

# 有时在已经解压的元组序列上 使用 enumerate()函数容易犯错，正确方式：
data = [(1,2),(3,4),(5,6),(7,8)]
# Correct:
for n,(x,y) in enumerate(data):
    print('{}:{}-{}'.format(n,x,y))

# Error:
for n,x,y in enumerate(data):
    print('{}:{}-{}'.format(n,x,y))
