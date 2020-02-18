#########################################################################
# File Name: 2_5_字符串搜索和替换.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Nov  5 16:05:46 2019
#########################################################################
#!/usr/bin/env python3

# 搜索 和 匹配 指定的文本模式
# 简单模式，str.replace() 方法 ：
text = 'yeah,but no,but yeah,but no,but yeah'
print(text.replace('yeah','yep'))

# 复杂模式，使用re中的sub() 函数。eg:将11/27/2012 形式的日期==> 2012-11-27：
text = 'Today is 11/27/2012.PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))
# sub(匹配模式，替换模式，) 反斜杠数字 指向匹配模式中的 组号

# 复用：
import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
ds = datepat.sub(r'\3-\1-\2',text)
print(ds)

# 更复杂的替换，    传递一个回调函数 来 代替。
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

ds = datepat.sub(change_date,text)
print(ds)

# 一个替换回调函数的参数 是一个match对象，也就是match() 或者 find() 返回的对象。
# 使用group() 方法 来提取特定的匹配部分，回调函数最后返回替换字符串
# 难点在于 编写 正则表达式。

# 多少替换发生，使用re.subn()
newtext,n = datepat.subn(r'\3-\1-\2',text)
print(newtext)
print(n)
