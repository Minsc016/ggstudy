#########################################################################
# File Name: 6_7_读写压缩文件.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: 2020年02月21日 星期五 10时58分04秒
#########################################################################
#!/usr/bin/env python3

# 读写一个 gzip 或 bz2 格式的压缩文件
# 解决方案
# gzip 和 bz2 模块 可以很容易的处理这些文件。两个模块都为open()函数提供了另外的实现来解决这个问题。比如，为了以文本形式读取压缩文件，可以：
# gzip compression

text = 'Sugar how you get so fly'


# 类似的，为了写入压缩数据，可以：
# gzip compression
import gzip
with gzip.open('somefile.gz','wt') as f:
    f.write(text)

# bz2 compression
import bz2
with bz2.open('somefile.bz2','wt') as f:
    f.write(text)

import gzip
with gzip.open('somefile.gz','rt') as f:
    text = f.read()
    print(text)

# bz2 compression
import bz2
with bz2.open('somefile.bz2','rt') as f:
    text = f.read()
    print(text)

# 如上，所有i/o操作都使用文本模式执行Unicode的编码/解码，类似的，
# 如果要操作二进制数据，使用rb 、wb 文件模式即可。

# 大部分情况下 读写压缩数据都是简单的。 
# 注意 选择一个正确的文件模式。
# 不指定模式，默认使用 二进制 模式。
# gzip.open() 和 bz2.open() 接受 跟内置open() 函数一样的参数。包括encoding,errors,newline等。


# 当写入压缩数据时，可以使用 compresslevel 这个可选关键字参数指定一个压缩级别。
with gzip.open('somefile.gz','wt',compresslevel=5) as f:
    f.write(text)

# 默认等级是9，即最高压缩等级。 等级越低 性能越好，但数据压缩程越低。
# 最后一点，gzip.open() 和 bz2.open() 罕为人知的特性：
# 作用在一个 已存在并以 二进制模式打开的文件上，下面代码可行：
import gzip
f = open('somefile.gz','rb')
with gzip.open(f,'rt') as g:
    text = g.read()
    print(text)
# //// f 用 rb 打开， g 用rt 打开。 f用rt的话会报错。

# 允许 gzip 和 bz2 模块 可以工作在许多 类文件对象上，比如套接字、管道、内存中文件等。
