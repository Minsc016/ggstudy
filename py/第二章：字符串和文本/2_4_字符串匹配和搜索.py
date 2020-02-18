#########################################################################
# File Name: 2_4_字符串匹配和搜索.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Nov  5 11:18:53 2019
#########################################################################
#!/usr/bin/env python3

# 匹配字面字符串 只需 基本字符串方法：str.find() str.endswith() str.startswith() 
text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')

# match start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# Search for the location of the first occurrence
print(text.find('no'))

# 复杂的匹配 使用 正则表达式 和 re模块
# eg匹配 数字格式的日期字符串 比如 11/27/2012:
text1 = '11/27/2012'
text2 = 'Nov 27,2012'
import re
# Simple matching:\d+ means one or more digits
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

# 如果想 使用 一个模式 做 多次匹配，应该先将 模式字符串 预编译 为 模式对象：
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# match() 总是从字符串开头去匹配，如果想 查找字符串任意部分的模式出现位置，用
# findall() 方法代替。：
text = 'Today is 11/27/2012.PyCon starts 3/13/2013'
print(datepat.findall(text))

# 定义正则表达式 的时候，通常会利用 括号取捕获分组：
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# 根据分组可以使得后面的处理 更加简单，因为可以分别将 每个组的内容提取出来
m = datepat.match('11/27/2012')
print(m)
# Extract the contents of each group
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

month,day,year = m.groups()
print(month,day,year)

# find all matches (notice splitting into tuples)
print(text)
datepat.findall(text)
for month,day,year in datepat.findall(text):
    print('{}-{:0>2}-{:0>2}'.format(year,month,day))

# findall() 方法 会 搜索文本并 以 列表 返回所欲的匹配，如果 想以迭代方法 返回匹配，可以
# 使用 finditer() 方法来代替:
for m in datepat.finditer(text):
    print(m.groups())

# 核心步骤：
# 1.使用 re.compile() 编译正则表达式字符串 
# 2.使用match()、findall()、finditer() 方法

# match() 仅仅检查字符串的开始部分：
m = datepat.match('11/27/2012abcdef')
print(m)
print(m.group())
# 精确匹配，正则表达式以 $　结尾
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))

# 仅仅做一次文本匹配/搜索操作：
print(re.findall(r'(\d+)/(\d+)/(\d+)',text))

