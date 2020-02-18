#########################################################################
# File Name: 2_14_合并拼接字符串.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Nov 14 19:54:34 2019
#########################################################################
#!/usr/bin/env python3

# 将几个小的字符串 合并为 一个大的字符串

# 如果 需要 合并的字符串 在一个序列 或者 iterable 中。那么，最快的方式是使用join() 方法
# 
parts = ['Is','Chicago','Not','Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

#ｊｏｉｎ　被指定为 字符串  的 一个方法。
# 连接的对象可能来自各种不同的数据序列，比如 列表、元组、字典、文件、集合、生成器。

# 如果只是 合并 少数 几个字符串，加号（+） ：
a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)

# + 操作符 在作为一些复杂字符串格式化的替代方案的时候  通常也工作的很好。
print('{} {}' .format(a,b))
print(a + ' ' + b)


# 如果 想在 源码 中 将 两个字面字符串 合并起来 ， 只需要放在一起
a = 'Hello' 'World'
print(a)

# 在 字符串格式化的时候 因 选择不当 会给应用程序带来严重性能损失
# 使用（+）加号连接大量字符串的时候是非常低效率的，因为加号连接
# 会引起内存复制 以及 垃圾回收操作。
# 尤其、不应该：
s = ' '
for p in parts:
    s += p
# 每执行一次 += 操作的时候 会 创建一个新的字符串对象。。。。。。。。。。。。。。。。
# 相对聪明的技巧，利用生成器表达式（-->1_19) 转换数据为字符串的同时合并字符串

data = ['ACME',50,91.1]
print(data)
print(' '.join(str(d) for d in data))
a,b,c = 'a','b','c'
# 注意不必要的字符串连接操作，比如打印：
print(a+':'+b+':'+c)  # Ugly
print(':'.join([a,b,c])) # Still Ugly
print(a,b,c,sep=':') # Better

f = open('./t.txt','a')
# 当混合使用 I/O 操作 和字符串连接操作的时候，有时  需要 仔细研究程序：
chunk1,chunk2 = 'fucking','holy shit'
# 下面两段代码：
# Version 1(string concatenation)
f.write(chunk1 + chunk2)

# Version 2(separate I/O operations)
f.write(chunk1)
f.write(chunk2)

# 如果两个字符串很小，第一个版本性能会更好。 因为 I/O 系统调用天生就慢。
# 如果两个字符串很大，那么第二个版本会更高效。 它避免了创建一个很大的临时结果并且要复制大量内存块数据。

# 根据实际决定。

# 构建 大量 小字符串 的输出代码，最好使用生成器函数，利用Yield语句产生输出片段

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

# 这种方法  并没有 对 输出片段到底怎样 组织作出假设。
# 可以用多种方法来合并

# join
text = ' '.join(sample())
print(text)
# 重定向到I/O
for part in sample():
    f.write(part)
# 结合I/O 的混合fang案：
def combine(source,maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ' '.join(parts)
            parts = []
            size = 0
        yield ' '.join(parts)
# 结合文件操作
with open('filename','w') as f:
    for part in combine(sample(),32768):
        f.write(part)
f.close()
# 关键在于原始 生成器函数并不需要知道使用细节，只负责 生成字符片段
