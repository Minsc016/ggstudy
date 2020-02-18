#########################################################################
# File Name: 2_15_字符串中插入变量.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Nov 20 16:45:08 2019
#########################################################################
#!/usr/bin/env python3

# 创建一个内嵌变量的字符串,变量被它的值所表示的字符串替换掉.
# 使用format

s = '{name} has {n} message'
print(s.format(name='Guido',n=37))

# 如果 要被替换的变量能在 变量域 中 找到，那么可以结合使用 format_map() 和 vars() 
name = 'Guido'
n = 37
print(s.format_map(vars()))

# vars() 还有一个特性： 它适用于对象实例。
class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n
a = Info('Guido',37)
print(s.format_map(vars(a)))

# format 和 format_map() 的一个缺陷就是 它们不能很好的处理 变量缺失的 情况，比如：
try:
    print(s.format(name = 'GUido'))
except KeyError as ke:
    print(ke)

# 避免这种错误的方法就是 另外定义一个含有 __missing__() 方法的字典对象，：
class safesub(dict):
    """防止 key 找不到"""
    def __missing__(self,key):
        return '{' + key + '}'

# 现在可以利用 这个类 包装输入后 传递给format_map():
del n # Make sure n is undefined
print(s.format_map(safesub(vars())))

# 如果频繁执行这些步骤，I可以将变量替换步骤用一个工具函数封装起来。
import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

# 然后可以：
name = 'Crow'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

# Python 缺乏 对变量替换的内置支持，导致各种不同的方案，：
# 1. 格式化
name = "Color"
n = 16
# the example is not work and didn't figer it out why
##################################################################################
# print('%(name) has %(n) messages.' % vars())                                   #
##################################################################################
# 2. 字符串模板
import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))



# foramt()  和 format_map() 相比这些，更加先进。 优先选择 .
# foramt() 方法还有一个好处就是      可以获得对 字符串格式化的所有支持（对齐、填充、数字格式化等）。
# 高级 特性---- 映射、字典类 中鲜为人知 的 __missing__()  方法可以定义如果处理缺失的值。

# 在 SafeSub类中，这个方法被定义为对缺失的值返回一个占位符。 
# 使缺失的值出现在结果字符串中，而不是产生一个KeyError异常。

# sub() 函数 使用 sys._getframe(1) 返回调用者的栈帧。
# 可以从中访问属性  f_locals 来获得局部变量。 
# 直接操作栈帧是不推荐的----单对于字符串替换工具，很有用。
# f_locals 是一个复制调用函数的本地变量的字典，改变f_locals 的内容 对后面 的变量访问没有任何影响。
# 虽说访问一个栈帧看上去很邪恶，但是对它的任何操作不会覆盖和改变调用者本地变量的值。
