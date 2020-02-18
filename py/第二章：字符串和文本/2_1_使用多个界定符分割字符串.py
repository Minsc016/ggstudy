########################################################################
# File Name: 2_1_使用多个界定符分割字符串.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Nov  4 11:12:45 2019
#########################################################################
#!/usr/bin/env python3

# 需要将一个字符串分割为多个字段； 但是分隔符 不固定。

# string 对象的split()方法 只适应于非常简单的字符串分割。
# 不允许有多个分隔符 或者 分隔符周围不确定的空格。
# 可 使用 re.split() 方法

line = 'asdf fjdk; afed,fjek,asdf,foo'
import re
print(re.split(r'[;,\s]\s*',line))

# 捕获分组
fields = re.split(r'(;|,|\s)\s*',line)
print(fields)

# 保留分割字符串：
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
#ｒｅｆｏｒｍ　ｔｈｅ　ｌｉｎｅ　ｕｓｉｎｇ　ｔｈｅ　ｓａｍｅ　ｄｅｌｉｍｉｔｅｒｓ
print(''.join(v+d for v,d in zip(values,delimiters)))
# 如果不想保留分割字符，单仍然需要括号 来 分组正则表达式的话：
print(re.split(r'(?:,|;|\s)\s*',line))

