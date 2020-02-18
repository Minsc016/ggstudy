#########################################################################
# File Name: 3_6_复数的数学运算.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Dec 13 09:20:41 2019
#########################################################################
#!/usr/bin/env python3

# 网络认证方案代码 需要使用 复数空间，、、、、 复数计算

# 复数keyi使用complex(real,imag) 或者 带有后缀j的浮点数来指定，：
a = complex(2,4)
b = 3 - 5j
print(a,b,sep='\t')

# 获取 对应的实部、虚部 和 共轭复数
print(a.real,a.imag,a.conjugate(),sep='\t')

# 数学运算
print(a+b,a*b,a/b,abs(a))

# 执行 其他的复数函数比如正弦、余弦、平方根，使用cmatch模块，
import cmath
print(cmath.sin(a),cmath.cos(a),cmath.exp(a),sep='\t')

# Python 中大部分与数学有关的模块都能处理复数。
# numpy, 构造一个复数数组 ，并执行各种操作。
import numpy as np
a = np.array([2+3j,4+5j,6-7j,8+9j])
print(a,a+2,np.sin(a),sep='\t')

# Python 的 标准数学函数 不能产生复数值，不会有复数返回值。
import math
try:
    math.sqrt(-1)
except ValueError as ve:
    print(ve)

import cmath
print(cmath.sqrt(-1))
