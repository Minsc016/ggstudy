#########################################################################
# File Name: 3_2_执行精确的浮点数运算.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 10 20:05:01 2019
#########################################################################
#!/usr/bin/env python3

# 需要对 浮点数 执行精确的计算操作， 并且不希望 有任何小误差的出现。

# 浮点数 普遍问题 不能精确表示 十进制 数。
a,b = 4.2,2.1
print(a+b == 6.3)
# 底层 CPU 和 IEEE 754 标准 通过自己的浮点单位去 执行算术时的特征。
# 由于 Python 的浮点数据类型使用底层 表示存储数据 ，误差没法避免。

# 如果要 更加精确（性能损耗），可以使用decimal 模块。

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)
print(a+b == 6.3)
print(a+b == Decimal('6.3'))
# decimal 模块 允许控制计算的每一方面，
# 包括数字位数 和 四舍五入 运算。
# 创建一个本地上下文 并 更改 它的设置：
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

# decimal 模块实现了 IBM 的 “通用小数运算规范”。 
# 有很多的配置选项。

# 如果做 科学计算、工程领域的计算，电脑绘图，科学领域大多数运算，
# 普通的浮点类型即可， 真实世界 中 很少会要求精确到 普通浮点数 提供的17位精度。
# 因此，误差允许； 计算快。

# 减法删除 以及 大数和小数的加分运算 所带来的影响。
nums = [1.23e+18,1,-1.23e+18]
print(sum(nums)) # Notice how 1 disappears
# 上面的错误 可以用 math.fsum() 所提供的更精确计算能力来解决：
import math
print(math.fsum(nums))
# 仔细 研究 各算法 误差 产生 来源
# decimal 主要用在 涉及 金融 的领域。 一点误差都不允许。 
