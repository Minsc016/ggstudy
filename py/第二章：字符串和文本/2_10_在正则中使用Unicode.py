#########################################################################
# File Name: 2_0_在正则中使用Unicode.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Nov 13 17:42:01 2019
#########################################################################
#!/usr/bin/env python3

# 正在使用 正则表达式 处理文本，但是关注 Unicode 字符处理。
# 默认情况下，re模块 已经 对一些Unicode 字符类游乐基本的支持。
# 比如，\\d 已经匹配任意Unicode数字了。

import re
num = re.compile('\d+')
# ASCII digits
print(num.match('123'))
# Arabic digits
print(num.match('\u0661\u0662\u0663'))

# 如果想再模式中 包含指定的Unicode 字符，可以使用 Unicode 字符对应的转义序列（比如\uFFF或者\UFFFFFFFF).
# 比如，一个匹配几个不同阿拉伯编码页面 中 所有字符的正则表达式
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# 当 执行搜索和匹配的时候，最好是先标准化并且清理所有文本为标准化格式。（-->2_9）
# 注意特殊情况，比如：忽略大小写匹配 和 大小写转换 的行为。
pat = re.compile('stra\u00dfe',re.IGNORECASE)
s= 'straße'
print('----')
print(s)
print(pat.match(s)) # Matches
print(pat.match(s.upper()) )# Doesn't match

print(pat.match(s.upper()) )# Doesn't match

print(s.upper() )# case folds

# 混合使用Unicode 和 正则表达式 最好安装第三库，
# 为Unicode 转换大小写 和 其他大量有趣特性 提供全面支持，包括模糊匹配。

