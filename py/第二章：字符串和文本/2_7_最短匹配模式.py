#########################################################################
# File Name: 2_7_最短匹配模式.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Nov 12 17:03:16 2019
#########################################################################
#!/usr/bin/env python3

# 用正则表达式 匹配某个文件模式，但是它找到的是模式的最长可能匹配；
# 修改它变成查找最短的可能匹配

# 解决方案：
# 一般匹配 一对分隔符 之间的文本的时候：
import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no".Phone says "yes"'
print(str_pat.findall(text2))

# r'\"(.*)\"' 匹配被双引号包含的文本。但是在正则表达式中 * 操作符是贪婪的，
# 因此匹配操作 会 查找最长的可能匹配。
# 所以 text2 中 返回结果 并不是我们想要的。

str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))

# 写包含点()字符的正则表达式的时候遇到的一些常见问题。
# . 匹配换行外的任何字符。
# 通过在 * 或者 + 这样的操作符后面添加一个? 可以强制匹配算法改成寻找最短的可能匹配
