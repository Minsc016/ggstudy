#########################################################################
# File Name: 2_11_删除字符串中不需要的字符.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Nov 14 10:46:08 2019
#########################################################################
#!/usr/bin/env python3

# 去掉文本字符串开头，结尾或者中间不想要的字符，比如空白

# strip() 方法 能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左/右执行删除
# 默认去除空格，可以指定其他字符。

# Whitespace stripping
s = ' hello world \n'
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '-----hello====='
print(t)
print(t.lstrip('-'))
print(t.strip('-='))

# strip() 方法在 读取和清理数据 以备后续处理的时候是经常会被用到的，
# 比如 可以用它们来去掉空格，引号和完成其他任务。
# 不会对字符串 的 中间文本产生任何影响。比如：
s = ' hello       world \n'
s = s.strip()
print(s)
# 处理中间的空格，需要其他方法，比如 replace() 或者 正则表达式
print(s.replace(' ',''))
import re
print(re.sub('\s+',' ',s))


# 将 strip() 操作 和 其他迭代操作 结合，比如从文件中读取多行数据
# 生成器表达式
with open ('./t.txt','r') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

# lines = line.strip() for line in f 执行数据转换操作，非常高效，不需要预先读取所有数据。
# 仅仅创建一个生成器，每次返回行之前会执行strip 操作

# 更高阶的strip，translate() 方法。-->2_12

