#########################################################################
# File Name: 3_12_基本日期时间转换.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Dec 23 11:07:04 2019
#########################################################################
#!/usr/bin/env python3

# 执行 简单的时间转换，天到秒，小时到分钟等。

# datetime 模块
# 表示时间段，可创建 一个 timedelta 实例：：：：
from datetime import timedelta
from datetime import datetime
a = timedelta(days = 2,hours = 6)
b = timedelta(hours = 4.5)
print(a,b,sep='\t')
c = a + b
print(c)

print(c.days)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds() / 3600)

# 表示指定日期和时间， 创建一个 datetime 实例 ； 然后使用标准数学运算 操作

# from datetime import datetime
a = datetime(2012,9,23)
print(a + timedelta(days=10))

b = datetime(2012,12,21)
print(b)
d = a - b
print(d)
print(d.days)

now = datetime.today()
print(now)

print( now + timedelta(minutes = 10))

# datetime 会自动处理闰年，比如
a = datetime(2012,3,1)
b = datetime(2012,2,28)
print(a-b)
print((a-b).days)
c = datetime(2013,3,1)
d = datetime(2013,2,28)
print((c-d).days)

# 处理时区、模糊时间范围、节假日计算等，使用dateutil模块
# 类似时间计算 可以使用 dateutil.relativedelta() 函数计算。
# PS：处理月份（天数差距） 的时候填充间隙

a = datetime(2012,9,23)
try:
    a + timedelta(months = 1)
except TypeError as te:
    print(te)

# from deteutil.relativedelta import relativedelta as rd
# print(a + rd(months=+1))

# Time between two dates
b = datetime(2012,12,21)
d = b - a
print(a,b,d)

# d = rd(b,a)
# print(d)
# print(d.months,d.days)

