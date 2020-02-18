#########################################################################
# File Name: 3_11_随机选择.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Dec 23 10:38:41 2019
#########################################################################
#!/usr/bin/env python3

# 从一个序列中 随机抽取若干元素，或者生成几个随机数。
# random 模块

import random
values = [1,2,3,4,5,6]
# 随机抽取,random.choice()
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

# 提取N个不同元素 random.sample()
print(random.sample(values,2))
print(random.sample(values,2))
print(random.sample(values,3))
print(random.sample(values,3))

# 打乱顺序
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)

# 生成随机整数，用random.randint()
for i in range(6):
    print(random.randint(0,10),sep='\t')

# 0到1 范围内均匀分布的浮点数，random.random()
for i in range(4):
    print(random.random(),sep='\n')

# 获取N位随机位（二进制）的整数，使用random.getrandbits()
print(random.getrandbits(200))

# random 模块 使用 Mersenne Twister 算法来计算生成随机数。
# 通过ｒａｎｄｏｍ．ｓｅeｄ（）　函数修改初始化种子。
random.seed() # Seed based on systerm time or os.urandom()
random.seed(12345) # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data


# 均匀分布、高斯分布、其他分布 的 随机数生成函数。
# random.uniform() 计算均匀分布随机数
# random.gauss() 计算正态分布随机数
# 在线文档。。。。。。。。
# 不应该用于密码学，类似功能使用 ssl 模块中相应函数，ssl.RAND_bytes() 生成安全随机字节序列。
