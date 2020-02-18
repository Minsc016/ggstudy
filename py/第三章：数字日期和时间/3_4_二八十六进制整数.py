#########################################################################
# File Name: 3_4_二八十六进制整数.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 10 20:50:41 2019
#########################################################################
#!/usr/bin/env python3

# 转换或者 输出 二进制、八进制、十六进制 整数。
# bin() oct hex() 函数
x = 1234
print('十进制\t二进制\t\t八进制\t十六进制')
print(x,bin(x),oct(x),hex(x),sep='\t')

# 不想输出前缀，使用 format() 函数
print(x,format(x,'b'),format(x,'o'),format(x,'x'),sep='\t')

x = -1234
# 有符号的整数， 处理负数的话  ， 输出结果会包含一个符号。
print(x,format(x,'b'),format(x,'o'),format(x,'x'),sep='\t')

# 产生无符号值， 需要增加一个指示最大长度的值，eg:为了显示32位的值：
print(format(2**32+x,'b'))
print(format(2**32+x,'o'))
print(format(2**32+x,'x'))

# 3. 为了以不同的进制转换整数字符串，简单的使用带有进制的int() 函数即可
print(int('4d2',16))
print(int('10011010010'),2)


# 大多数情况下处理二进制、八进制、十六进制 整数是很简单的，
#只需要记住这些转换属于整数和其对应的文本表示之间的转换即可，
#　永远至右一种整数类型。

# 使用八进制：：：： Python 指定八进制数的语法 跟 其他语言不通，比如
# 如果 下面 方法指定 八进制，会出现语法错误：
import os
#os.chmod('script.py',0755)
#需要确保 八进制 的前缀是Oo,:::
os.chmod('script.py',0o755)
