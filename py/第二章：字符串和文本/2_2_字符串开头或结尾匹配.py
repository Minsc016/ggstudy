#########################################################################
# File Name: 2_2_字符串开头或结尾匹配.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Nov  4 16:56:31 2019
#########################################################################
#!/usr/bin/env python3

# 通过指定文本模式  去 检查 字符串的开头 或者 结尾，比如文件名后缀，URL，Scheme等。
# 检查字符串开头或结尾的一个简单方法 是使用 str.startwith() str.endwith()方法

filename = 'spam.txt'
print(filename.endswith('txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

# 如果想 检查多种匹配 可能，只需要 将所有 匹配项 放入到一个元组中取，然后传给startswith()或者endswith()方法。
import os
filename = os.listdir('.')
print(filename)

print([name for name in filename if name.endswith(('.py','.py~'))])
print(any(name.endswith('.py') for name in filename))

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# if __name__ == '__main__':
#     read_data(input("请输入链接（无网络不可用）"))

# startswith 和 endswith 必须接收元组/字符串作为函数,如果是列表/集合 先转成tuple
# 也可以用用切片
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:5] == 'https:' or url[5] == 'ftp:')

# 或者正则表达式
import re
print(re.match('http:|https:|ftp:',url))

# 当和 其他操作 比如 普通数据聚合相结合的时候，startwith() 和 endswith() 方法很不错。
# 检查文件夹中是否存在 指定 的文件类型
# if any(name.endswith(('.c','.h')) for name in listdir(dirname)):
#     ...........
