#########################################################################
# File Name: 4_3_使用生成器创建新的迭代模式.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 24 17:18:00 2019
#########################################################################
#!/usr/bin/env python3

# 实现一个自定义 迭代模式，    跟普通的内置函数比如
# range()，reversed() 不一样。

# 解决方案
# 实现一种新的迭代模式，使用一个生成器函数来定义它。
# 生成某个范围内浮点数的生成器。
def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x
        x += increment

# 使用for 循环 迭代它 或者 使用其他接受一个可迭代对象的函数，比如 sum(),list()
for n in frange(0,4,0.5):
    print(n)

print(list(frange(0,4,0.5)))

# 一个函数中需要有一个yield语句，即可将其转换为一个生成器。
# 跟普通函数不同的是，生成器只能用于迭代操作。
# 底层工作机制

def countdown(n):
    print('Starting to count from',n)
    while n > 0:
        yield n
        n -= 1
    print("Done")

# Create the generator, notice no output appears
c = countdown(3)
print(c)
# Run to first yield and emit a value
print(next(c))

# Run to the next yield
print(next(c))

# Run to next yield
print(next(c))

# Run to next yield (iteration stops)
print(next(c))

# 一个生成器函数主要特征是它 只会回应在迭代中使用的next操作
# 一旦生成器函数返回退出，迭代终止。
# 在迭代中通常使用的for语句 会自动处理细节。
