#########################################################################
# File Name: 1_8_字典的运算.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Oct 23 15:38:08 2019
#########################################################################
#!/usr/bin/env python3

# 数据字典中 求  最小值、最大值、排序 等运算

prices = {
        'ACME':45.23,
        'AAPL':612.78,
        'IBM':205.55,
        'HPQ':37.20,
        'FB':10.75
        }

# 为了 堆 字典值 进行计算操作，通常需要用zip函数 把 键和值 反过来，
min_price = min(zip(prices.values(),prices.keys()))
# min_price is (10.75,'FB')
max_price = max(zip(prices.values(),prices.keys()))
# max_price is (612.78,'AAPL')

# 类似的，可以使用zip()和sorted 来排序字典数据
print(sorted(zip(prices.values(),prices.keys())))

# zip 函数 创建 的 是 只能访问一次 的 迭代器
prices_and_names = zip(prices.values(),prices.keys())
print(min(prices_and_names)) # OK
try:
    print(max(prices_and_names)) # ValueError
except ValueError as E:
    print('Value Error,shows that zip() object is a iterator')

##########################################################################################
# 在普通字典上 使用 数学运算，要合理使用key 参数
print(min(prices,key = lambda k:prices[k]) )# returns 'FB'
max(prices,key = lambda k:prices[k])

# zip 翻转 键值
# 如果值相同，会比较键。
