#########################################################################
# File Name: 1_11_命名切片.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Oct 23 17:39:03 2019
#########################################################################
#!/usr/bin/env python3

# 硬编码下标 清理 成 命名切片

record = '............................100..................513.25..................'
# 无法直视 示范：
cost = int(record[28:31]) * float(record[49:55])
print(cost)
# 命名切片
SHARES = slice(28,31)
PRICE = slice(49,55)
cost = int(record[SHARES]) * float (record[PRICE])
print(cost)
# 避免了大量无法理解 的 硬编码下标，使得代码清晰可读。
items = [ 0,1,2,3,4,5,6,7,8]
a=slice(2,4)
print(items[2:4],items[a])

print("--------")
print(items)
del items[a]
print(items)

# 切片对象a ：  调用a.start,a.stop,a.step 属性
a = slice(5,50,2)
print(a.indices)
print(a.start,a.stop,a.step)
s = 'Hello World'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])


