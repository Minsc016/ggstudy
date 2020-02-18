#########################################################################
# File Name: 3_15_字符串转为日期.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 24 11:16:18 2019
#########################################################################
#!/usr/bin/env python3

# 应用程序接受 字符串格式的输入， 将它们转换为datetime对象 以便在上面执行非字符串操作。

# 解决方案：
# 使用 Python 的标准模块 datetime。
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text,'%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

# datetime.strptime() 方法
# 支持很多 格式化 代码
# %Y 4位数年份
# %m 2位数月份
# 格式化占位符顺序可以反过来
# 比如，一个datetime对象，想将它格式化为漂亮易读形式后放在自动生成的信件或报告的顶部

print(z)
nice_z = datetime.strftime(z,'%A %B %d, %Y')
print(nice_z)

# strptime() 的性能 很差，使用纯Python实现，必须处理所有系统本地设置。
# 如果需要在代码中解析大量日期 并且已经知道了日期字符串的确切格式，
# 可以自己实现一套解析方案来获取更好的性能。
# 比如，已知，日期格式都为 YYYY-MM-DD,::::解析函数：：：：

def parse_ymd(s):
    year_s,mon_s,day_s = s.split('-')
    return datetime(int(year_s),int(mon_s),int(day_s))

print(parse_ymd(text))



# 实测中，此函数比strptime() 快7倍多。
def parse_ymd(s):
    year_s,mon_s,day_s = s.split('-')
    dt = datetime(int(year_s),int(mon_s),int(day_s))
    return datetime.strftime(dt,"%A %B %d, %Y")

print(parse_ymd(text))
