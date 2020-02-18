#########################################################################
# File Name: 5_3_使用其他分隔符或行终止符打印.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Jan 17 10:52:09 2020
#########################################################################
#!/usr/bin/env python3

# 想 使用 print() 函数 输出数据，但是想改变默认的分隔符或者行尾符。
# 在print() 函数中使用 sep 和 end 关键字参数
print('ACME',50,91.5)
print('ACME',50,91.5,sep=',')
print('ACME',50,91.5,sep=',',end='!!\n')

# 使用end 参数也可以在输出中禁止换行，比如
for i in range(5):
    print(i)

for i in range(5):
    print(i,end=' ')

# 使用 非空格分隔符来输出数据的时候，给print() 函数传递一个sep参数是最简单的方案。
# 有时候你会看到一些程序员会使用str.join() 来完成同样的事情。

print(','.join(('ACME','50','91.5')))
# str.join() 问题在于仅仅适用于字符串，
# 意味着 通常需要执行另外一些转换才能让它正常工作。
row = ('ACME',50,91.5)
try:
    ','.join(row)
except TypeError as te:
    print(te)

print(','.join(str(x) for x in row))

# 当然：
print(*row,sep=',')
