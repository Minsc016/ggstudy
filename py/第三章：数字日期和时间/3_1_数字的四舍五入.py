#########################################################################
# File Name: 3_1_数字的四舍五入.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 10 17:48:16 2019
#########################################################################
#!/usr/bin/env python3

# 对 浮点数 执行指定 精度的舍入运算
# 1.简单的，round(value,ndigits)
print(round(1.24,1))
print(round(1.25,1))
print(round(1.26,1))

# 当一个值刚好在两个边界的中间的时候，round函数返回离他最近的偶数。
# 1.5 和 2.5 的舍入运算都是 2   3.5 和 4.5 都是4 ……

# 传给 round() 函数的ndigits 参数可以使负数，
# 摄入运算会作用在 十位 百位 千位 上面。
a = 3360
print(round(a,-1))
print(round(a,-2))
print(round(a,-3))

# 舍入 不同于 格式化
x = 1.23456
print(format(x,'0.1f'))
print(format(x,'0.2f'))
print(format(x,'0.3f'))
print('value is {:0.3f}'.format(x))

# 不要 舍入 浮点值 来修正 浮点精度问题：
a = 2.1
b = 4.2
c = a + b
print(c,round(c,2),sep='\t') # "fix" result???
# 对于 大多数 使用 浮点的程序， 没有必要也不推荐 这样做。
# 尽管计算时会有小误差。
# 如果不允许误差，则使用 decimal 模块。-->3_2
