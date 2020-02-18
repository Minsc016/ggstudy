#########################################################################
# File Name: 2_13_字符串对齐.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Nov 14 19:39:48 2019
#########################################################################
#!/usr/bin/env python3

# 通过某种对齐方式 来 格式化字符串
# 1.基本的字符串对齐操作，可以使用字符串的ljust()，rjust()和center() 方法
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 这些 方法 都可以接受 一个可选 填充字符，比如：
print(text.rjust(20,'='))
print(text.center(20,'*'))

# format() 同样可以 很容易的 对齐字符串。 使用 <  >  ^  跟一个宽度：
print('-------')
print('{:>20}'.format(text))
print(format(text,'>20'))
print('-'*8)
print(format(text,'<20'))
print(format(text,'^20'))

# 指定一个 非 空格的填充字符，写到对齐字符的签名即可。
print(format(text,'=>20s'))
print(format(text,'*^20s'))

# 格式化多个值，使用format:
print('{:->10s} {:=>10s}'.format('Hello','World'))
# format 不仅适用于字符串，     它可以格式化 任何值。 eg数字：
x = 1.2345
print(format(x,'>10'))
print(format(x,'^10.2f'))

# 古老的代码 中 % 操作符 格式化文本：
print('%-20s' % text)
print('%20s' % text)

# 新版本代码中， 优先选择format() 函数 或者 方法。
# format() 要比 % 操作符 功能更为强大。
# format() 比 ljust() rjust() center() 更通用。
# format -->Python在线文档  说明 具体用法
