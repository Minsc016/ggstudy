#########################################################################
# File Name: 1_19_转换并同时计算数据.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Oct 29 19:53:29 2019
#########################################################################
#!/usr/bin/env python3

# 在数据序列上 执行 聚集函数（比如sum()、min()、max() )，但是首先你需要先转换：
# 在 数据序列 上 执行 聚集函数（sum()、min()、max()），之前 转换/过滤 数据

# 计算平方和
nums = [1,2,3,4,5]
s = sum(x*x for x in nums)
print(s)

import os
files = os.listdir('.')
#  Determine if any .py files in directory
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry,no python')

# Output a tuple as CSV
s = ('ACME',50,123.45)
print(','.join(str(x) for x in s))

#Data reduction across fields of a data structure
portfolio = [
        {'name':'GOOD','shares':50},
        {'name':'YHOO','shares':75},
        {'name':'AOL','shares':20},
        {'name':'SCOX','shares':65}
        ]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# 当 生成器表达式 作为一个 单独参数 传递给函数时候的巧妙语法。eg：
s = sum((x * x for x in nums))
s = sum(x *x for x in nums) #更加优雅
# 使用 生成器表达式 作为参数 比 创建一个临时列表 更加高效和优雅
# 
nums = [1,2,3,4,5]
s = sum([x *x for x in nums])
# 这样多一个 创建额外列表的步骤，如果元素数量非常大，会创建一个巨大的仅仅使用一次就被丢弃的临时数据结构。
# 而生成器方案会以迭代的方式 转换 数据，更省内存。

# 聚集函数 使用生成器版本 。  key 关键字参数
# Original : Return 20
print(min(s['shares'] for s in portfolio))
# Alternative : Returns {'name':'AOL','shares':20}
print(min(portfolio,key = lambda s:s['shares']))
from operator import itemgetter
print(min(portfolio,key = itemgetter('shares')))

