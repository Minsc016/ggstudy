#########################################################################
# File Name: 3_13_计算最后一个周五的日期.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Dec 23 14:38:30 2019
#########################################################################
#!/usr/bin/env python3


# 查找 星期中 某一天 最后出现的日期，比如星期五。

#　ｄａｔｅｔｉｍｅ
# 通用方案
from datetime import datetime,timedelta
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def get_previous_byday(dayname,start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days = days_ago)
    return target_date

print(datetime.today() )
print(get_previous_byday('Monday'),get_previous_byday('Tuesday'),get_previous_byday('Wednesday'),get_previous_byday('Thursday'),get_previous_byday('Friday'),get_previous_byday('Saturday'),get_previous_byday('Sunday'),sep='\n')

# 先将 开始日期 和目标日期 映射到 星期数组的位置上，星期一索引为0，
# 然后通过模运算 计算出目标日期要经过多少天到达开始日期
# 然后用开始日期 减去 时间差 得到 目标日期

# 如果有大量日期运算，使用python-dateutil第三方包来代替
# 使用  timeutil.ralativedelta() 函数执行

####from datetime import datetime
####from dateutil.relativedelta import relativedelta
####from dateutil.rrule import *
####
####d = datetime.now()
####print(d)
####
##### Next Friday
####print(d + relativedelta(weekday = FR))
####
##### last Friday
####print(d + relativedelta(weekday = FR(-1)))
