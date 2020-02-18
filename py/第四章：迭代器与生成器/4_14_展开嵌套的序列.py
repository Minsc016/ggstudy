#########################################################################
# File Name: 4_14_展开嵌套的序列.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Jan 14 11:16:27 2020
#########################################################################
#!/usr/bin/env python3
# 将一个多层嵌套的序列展开成一个单层列表
from collections import Iterable

def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1,2,[3,4,[5,6],7],8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x,end=' ')
print('\n')

# isinstance(x,Iterable) 检查某个元素是否可迭代的。如果是，
# yield from 就会返回所有 子例程的值。
# 最终返回结果就是一个没有嵌套的简单序列。

# 额外的参数 ignore_types 和 检测语句 isinstance(x,ignore_types) 用来将字符串和字节排除在
# 可迭代对象外，防止将它们再展开成单个的字符。 
# 字符串数组 最终返回结果。

items = ['Dave','Paula',['Thomas','Lewis']]
for x in flatten(items):
    print(x)

# 语句 yield from 在生成器中调用其他生成器作为子例程时非常有用。
# 如果不适用 yield from ，就得写额外的for循环
def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x

# 尽管 只 改了一点，但是 yield from 语句看上去感觉更好，并且也使代码更简洁。
# 对于字符串 和 字节的额外检查 就是为了防止将它们再展开成单个字符，如果还有其他不想展开的类型，修改参数ignore_types即可。
# 最后要注意的一点是，yield from 在涉及到基于协程 和 生成器的并发编程中扮演着更加重要的角色。
# 参考 12_12
