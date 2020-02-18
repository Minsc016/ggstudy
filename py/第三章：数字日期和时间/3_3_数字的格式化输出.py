#########################################################################
# File Name: 3_3_数字的格式化输出.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 10 20:31:22 2019
#########################################################################
#!/usr/bin/env python3

# 需要 将 数字格式化 后 输出， 控制数字的 位数、对齐、千位分隔符 和 其他细节。

#1. 格式化单个数字，可以使用内置format()
x = 1234.56789
# Two decimal places of accuracy
print(format(x,'0.2f'))

# Right justified in 10 chars,one-digit accuracy
print(format(x,'>10.1f'))
print(format(x,'<10.1f')) # Left justified
print(format(x,'^10.1f')) # Centered

print(format(x,',')) # Inclusion of thousands separator
print(format(x,'0,.1f')) # 

# 同时 指定 宽度 和 精度 的一般形式 是 '[<>^]?width[,]?(.digits)?',
# 其中 width 和 digits 为整数， ？ 表示可选部分。 
# 同样的格式也被用在字符串的 format() 方法中。
print('the value is (:0,.2f)'.format(x))

# 适用于 浮点数 和 decimal 模块中的Decimal 数字对象。
# 指定 数字位数后， 结果值 会根据 round() 函数 同样的 规则 进行四舍五入 后返回。
print(x)
print(format(x,'0.1f'))
print(format(-x,'0.1f'))


# 包含千位符的格式化跟本地化没有关系。
# 如果需要根据地区 显示 千位符， 需要自己调查 locale 模块中的函数。
# 也可以 使用字符串的 translate() 方法 来交换千位符。
swap_separators = {ord('.'):',',ord(','):'.'}
print(format(x,',').translate(swap_separators))

# 2. % 格式化
print('%0.2f' % x)
print('%10.1f' % x )
print("%-10.1f" % x)

# 不如 format 方法先进，一些特性不被支持。
