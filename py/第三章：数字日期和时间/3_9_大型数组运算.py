#########################################################################
# File Name: 3_9_大型数组运算.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Dec 20 14:46:38 2019
#########################################################################
#!/usr/bin/env python3

# 在 大数据集（数组/网络）上执行计算，
# 数组的 重量级 运算操作，可以使用 NumPy库。
# Numpy会给Python提供一个数组对象，比标准的Python列表更适合 数学运算。

# Python lists
x = [1,2,3,4]
y = [5,6,7,8]
print(x*2)
try:
    x+10
except TypeError as te:
    print(te)

print(x+y)

# Numpy lists
import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)


# Numpy 中的标量运算 会 作用在每一个元素上。
# 当两个操作数 都是 数组的时候 执行元素对等位置计算，并最终生成一个新的数组。

# 对整个数组中所有元素 同时 执行数学运算可以使得 作用在整个数组上的函数运算简单而又快速。
# 计算多项式：
def f(x):
    return 3*x**2 - 2*x + 7

print(f(ax))

# numpy 还为数组 操作提供了大量的通用函数，这些函数可以作为math模块中类似函数的替代，
print(np.sqrt(ax))
print(np.cos(ax))

# 底层实现中，Numpy 数组使用了C或者Fortran语言的机制分配内存。
# 是一个非常大的连续的并由同类型数据组成的内存区域。

# 可以构造一个比普通Python列表大的多的数组。

# 浮点数 二维网络：：：： 10000 * 10000

grid = np.zeros(shape = (10000,10000),dtype = float)
print(grid)

# 所有普通操作会同时作用在所有元素上。
grid += 10
print(grid)

print(np.sin(grid))

# Numpy 扩展Python列表的索引功能----特别是对于多维数组。
# 试验（简单的二维数组）：

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
# select row 1
print(a[1])
# select column 1
print(a[:,1])
# Select a subregion and change it
print(a[1:3,1:3])
a[1:3,1:3] += 10
print(a)

# Broadcast a row vector across an operation on all rows
print( a + [100,101,102,103] )
print(a)
# Conditional assignment on an array
print(np.where(a<10,a,10))

# NumPy 是 Python 领域中 很多科学与工程库的基础。http://www.numpy.org
