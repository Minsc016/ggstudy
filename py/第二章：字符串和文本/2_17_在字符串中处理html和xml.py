#########################################################################
# File Name: 2_17_在字符串中处理html和xml.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Nov 21 17:50:18 2019
#########################################################################
#!/usr/bin/env python3

# 将 HTML 或者 XML ，实体如 &entity;或 &#code;
# 替换为对应的文本。再者，你需要转换文本中特定的字符（比如<,>,或&）。

# 替换 文本字符串中 的 '<' '>' ，使用html.escape()函数 。
s = 'Elements are written as "<tag>text</tag>".'

import html
print(s)
print(html.escape(s))

# DIsable escaping of quotes
print(html.escape(s,quote=False))

# 为了替换文本中的编码实体， 需要使用另外一种方法。
# 使用一个合适的HTML 或 XML 解析器，这些工具会自动替换编码值。
# 含有编码值的原始文本，手动替换。---- 使用解析器的相关函数即可。：
s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))

t = 'The promt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))

# 在 生成 HTML 或者 XML 文本的时候，如何正确的转换特殊标记字符 是 一个很容易
# 被忽视的细节。 特别是当你使用 print() 函数 或者 其他字符串格式化 来 产生输出的时候
# 使用像 html.escape() 的工具函数可以很容易的解决这类问题

# 其他方式处理文本，工具函数比如 xml.sax.saxutils,unescapge() 
# 应先调研清楚如果使用一个合适的解析器
# 处理HTML 或 XML 文本，使用某个解析模块 html.parse 或 XML.etree.ElementTree 
# 已经自动处理了相关的替换细节。
