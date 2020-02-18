#########################################################################
# File Name: 2_16_以指定列宽格式化字符串.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Nov 21 16:15:51 2019
#########################################################################
#!/usr/bin/env python3

# 有一些长字符串，想以 指定的列宽将它们重新格式化
# 使用 texttrap 模块 格式化字符串的输出。
s = "Look into my eyes,look into my eyes,the eyes,the eyes,\
        the eyes,not around the eyes,dont look around the eyes,\
        look into my eyes,you're under"

import textwrap
print(textwrap.fill(s,70))
print(textwrap.fill(s,40))
print(textwrap.fill(s,40,initial_indent='    '))
print(textwrap.fill(s,40,subsequent_indent='    '))


# textwrap 模块对于字符串打印 是非常有用的， 特别是当 希望输出自动匹配终端大小的时候
# 使用 os.get_teminal_size() 方法来获取终端的大小尺寸。比如
import os
print(os.get_terminal_size())

# fill() 方法接受 一些其他可选参数来控制tab，语句结尾等。
# 参阅 textwrap TextWrapper
