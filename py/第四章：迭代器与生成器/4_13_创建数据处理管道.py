#########################################################################
# File Name: 4_13_创建数据处理管道.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Dec 30 11:51:06 2019
#########################################################################
#!/usr/bin/env python3


# 数据管道（类似Unix管道） 的方式 迭代处理数据。
# 比如，大量数据需要处理，但是不能将 它们一次性放入内存中。

# 生成器函数 是一个实现管道机制的好办法。eg,假设要处理一个非常大的日志文件目录。

# 定义一个由多个执行特定任务独立任务的简单生成器函数组成的容器。
import os
import fnmatch
import gzip
import bz2
import re

# 找文件 并 生成路径
def gen_find(filepat,top):
    '''
    Find all filenames in a directory tree that match a shell wildcart pattern
    '''
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)
def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object
    The file is closed  immediately when proceeding to the next iteration
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename,'rt')
        elif filename.endswith('.bz2'):
           f = bz2.open(filename,'rt')
        else:
            f = open(filename,'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern,lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

lognames = gen_find('access-log*','www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python',lines)
for line in pylines:
    print(line)
