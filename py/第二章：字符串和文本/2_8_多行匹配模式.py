#########################################################################
# File Name: 2_8_多行匹配模式.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Nov 13 11:38:47 2019
#########################################################################
#!/usr/bin/env python3

# 用 正则表达式 匹配 一大块文本 ，需要 跨行 匹配
# eg: 比配 C语言 分割的注释

import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */'''

print(comment.findall(text1))
print(comment.findall(text2))

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# (?:.|\n) 指定了一个非捕获组，它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组

# re.compile() 函数接受一个 标志参数 叫 re.DOTALL ，可以让 正则表达式 中的点（）匹配
# 包包括换行符在内的任意字符。比如：
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment.findall(text2))

# 对于简单的情况 使用re.DOTALL 标记参数工作的很好，
# 但如果模式非常复杂或者为了构造字符串令牌而将多个模式合并起来（--2_18)
# 使用这个标记参数可能出现一些问题，
# 定义自己的表达式模式 较好，可以在不需要额外的标记参数下也能很好的工作。
