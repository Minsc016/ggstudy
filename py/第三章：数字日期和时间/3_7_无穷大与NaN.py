#########################################################################
# File Name: 3_7_无穷大与NaN.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Dec 13 10:03:23 2019
#########################################################################
#!/usr/bin/env python3

# 创建或测试正无穷、负无穷、NaN（非数字）的浮点数。
a = float('inf')
b = float('-inf')
c = float('nan')

# 测试这些值的存在，使用math.isinf() 和 math.isnan() 函数，
import math
print(math.isinf(a))
print(math.isnan(c))
# 更多信息，参考IEEE 754规范。
# 无穷大数 数学计算
a = float('inf')
print(a+45,a*10,10/a,sep='\t')

# 有些操作时 未定义的 并 会返回一个NaN 结果，比如：
a = float('inf')
print(a / a)

b = float('-inf')
print(a + b)

# NaN值 会在所有操作中传播，而不会产生异常，
c = float('nan')
print(c+23,c/2,c*2,math.sqrt(c),sep='\t')

# NaN值的一个特别的地方时它们之间的比较操作总是返回False，
c = float('nan')
d = float('nan')
print(c == d,c is d,sep='\t')

# 测试一个NaN值的 唯一安全的方法就是使用 math.isnan() 
# 若要改变 Python 默认行为，在返回无穷大 或 NaN结果的操作中抛出异常。
# fpectl 模块可以用来改变这种行为，但是它在标准的Python构建中并没有被启用
# 针对平台相关，专家级程序员。####参考在线Python文档 for more details####
