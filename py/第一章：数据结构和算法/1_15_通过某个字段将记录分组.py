#########################################################################
# File Name: 1_15_通过某个字段将记录分组.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 24 10:56:09 2019
#########################################################################
#!/usr/bin/env python3

rows=[
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]
# 在date 分组后 的 数据块上 进行迭代
# 1.首先 按照指定的字段 (date) 排序
# 2.调用itertools.groupby()函数：
from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key = itemgetter('date'))
# Iterate in groups
for date,items in groupby(rows,key = itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# groupby() 函数 扫描 整个序列并且查找 连续相同值 。
# 每次迭代 返回一个值 和 一个迭代器对象， 迭代器中的对象都是 值 这个组里的。
# 事先排序
#　根据 date 字段将 数据分组到一个大的数据结构中取，并允许随机访问，：defaultdict()
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for group in rows_by_date:
    print(group)
    for row in rows_by_date[group]:
        print(' ',row)
####

