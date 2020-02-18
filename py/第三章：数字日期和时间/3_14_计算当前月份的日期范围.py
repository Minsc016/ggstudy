#########################################################################
# File Name: 3_14_计算当前月份的日期范围.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 24 09:39:44 2019
#########################################################################
#!/usr/bin/env python3

# 需在 当前月份 中 循环每一天，找到一个计算这个日期范围的高效方法。
# 解决方案：
# 1. 事先构造一个包含所有日期的列表。
# 2.计算出开始日期和结束日期
# 3.用 datetime.timedelta 步进，递增日期变量。
#### 一个接受任意 datetime 对象并返回一个由当前月份开始 和 下个月 开始日 组成的元组对象。

from datetime import datetime,date,timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _,days_in_month = calendar.monthrange(start_date.year,start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date,end_date)

a_day = timedelta(days=1)
first_day,last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

# 先计算出一个 对应月份第一天的日期
# 使用 date 或者 datetime 对象的 replace() 方法 将 days属性设置成1
# replace() 方法 会创建一个和 传入对象 类型相同的对象
# 传入date，结果也是date；

# 然后，使用calendar.monthrange() 函数来找出该月的总天数。
# monthrange() 函数会返回包含星期 和 该月 天数的元组。

# 结束日期 可以通过在开始日期 上 加 天数获得。 
# 结束日期是下个月开始日期；
# 和Python 的 slice 、 range 操作行为一致，不包含结尾。。

# 使用 标准的数学和比较操作 在 日期范围上循环
# 利用 timedelta 递增日期，小于号 < 用来检查一个日期是否在结束日期之前。


### 理想情况，为日期迭代一个同内置的range() 函数一样的函数。 
# 可以使用生成器 实现目标。


def date_range(start,stop,step):
    while start < stop:
        yield start
        start += step

# 使用
for d in date_range(datetime(2012,9,1),datetime(2012,10,1),timedelta(hours=6)):
    print(d)


# Python中 日期和时间 能够使用标准 数学和比较操作  进行预算。
