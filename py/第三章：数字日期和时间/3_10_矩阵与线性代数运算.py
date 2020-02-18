#########################################################################
# File Name: 3_10_矩阵与线性代数运算.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Dec 20 15:28:17 2019
#########################################################################
#!/usr/bin/env python3

# 你需要执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式求解先行方程组等。

# Numpy 库 矩阵对象
import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)

# Return transpose
print(m.T)

# Return reverse
print(m.I)

# Create a vector and multiply
v = np.matrix([[2],[3],[4]])
print(v)

print(m * v)

# 可以在numpy.linalg 子包 中找到更多的操作函数
import numpy.linalg
# determinant
print(numpy.linalg.det(m))

# Eigenvalues
print(numpy.linalg.eigvals(m))

# Solve for x in mx = v
x = numpy.linalg.solve(m,v)
print(x)
print(m * x)
print(v)

# 线性代数 是个 非常大的主题。
# Numpy 对 操作数组 和 向量 是一个很好的入口点。

