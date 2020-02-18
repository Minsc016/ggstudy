#########################################################################
# File Name: 1_17_从字典中提取子集.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Oct 28 10:12:20 2019
#########################################################################
#!/usr/bin/env python3

# 构造一个字典， 它是另外一个字典的子集
prices = {
        'ACME':45.23,
        'AAPL':612.78,
        'IBM':205.55,
        'HPQ':37.20,
        'FB':10.75
                }

# Make a dictionary of all prices over 200
p1 = {key:value for key,value in prices.items() if value > 200}
# make a dictionary of tech stocks
tech_names = {'AAPL','IBM','HPQ','MSFT'}
p2 = {key:value for key,value in prices.items() if key in tech_names}

print(p1,'\n',p2)

# 字典推导
# 通过创建一个元组序列 然后把它传给dict()函数
p3 = dict((key,value) for key,value in prices.items() if value > 200)
print(p3)
# 字典推导 更快
p2 = { key:prices[key] for key in prices.keys() & tech_names}
print(p2) # 话费时间多，约为第一种的1.6倍
