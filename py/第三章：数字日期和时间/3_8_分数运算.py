#########################################################################
# File Name: 3_8_分数运算.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Dec 13 10:47:54 2019
#########################################################################
#!/usr/bin/env python3

# 小学家庭作业 //// 木工工厂的测量值         分数运算

# fractions 模块可以被用来执行包含分数的数学运算。
from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)
print(a+b,a*b,sep='\t')

# Getting numerator/denominator
c = a*b
print(c,c.numerator,c.denominator,sep='\t')

# Converting to a float
print(float(c))

# Limiting the denominator of a value
print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
