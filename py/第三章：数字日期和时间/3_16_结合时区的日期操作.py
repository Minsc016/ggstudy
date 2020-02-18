#########################################################################
# File Name: 3_16_结合时区的日期操作.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 24 11:45:52 2019
#########################################################################
#!/usr/bin/env python3

# 你有一个安排在 2012 年 12 月 21日 早上9:30 的电话会议，地点 在芝加哥。
# 而你的朋友在印度的班加罗尔，那么它应该在当地几点参加会议？

# 解决方案
# 时区：    ｐｙｔｚ　模块。
# 提供了 Olson时区数据库，是时区信息的事实上的标准，在很多语言、操作系统都有。
# pytz 模块 一个主要用途 将 datetime 库创建的简单日期对象本地化。
# 示例： 表示一个芝加哥时间。
from datetime import datetime,timedelta
from pytz import timezone

d = datetime(2012,12,21,9,30,0)
print(d)

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# 一旦 日期被本地化， 就可以 转换为其他时区的时间 了。
# 班加罗尔；
#　Ｃｏｎｖｅｒｔ　ｔｏ　ｂａｎｇａｌｏｒｅ　ｔｉｍｅ
band_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(band_d)

#本地化日期上　执行计算　需要特别注意　夏令时转换　和其他细节。
# 2013 年，美国标准夏令时时间开始于本地时间 3月10日 凌晨2:00
# 在那时，时间向前跳过1小时。
# 如果在执行本地计算，会得到一个错误。
d = datetime(2013,3,10,1,45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes = 30)
print(later)

# 结果错误是因为没有考虑在本地时间中有1小时的跳跃，修正：
# 使用时区对象的normalize() 方法
later =central.normalize(loc_d + timedelta(minutes = 30))
print(later)

print('\n\n')
# 为避免晕头转向，处理本地化日期 通常策略： 先将所有日期转换为UTC时间，并用它执行所有的中间存储和操作。
import pytz
print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)


# 转换为UTC，不用担心夏令时问题。
# 可以执行 常见日期计算， 使用合适的时区转换输出本地时间
later_utc = utc_d + timedelta(minutes = 30)
print(later_utc.astimezone(central))

# 当设计时区操作的时候，有个问题就是如何得到时区的名称。
# 比如印度时区名“Asia/Kolkata”，为了查找，可以使用ISO 3166 国家代码作为关键字查询字典pytz.country_timezones.

print(pytz.country_timezones('IN'))
