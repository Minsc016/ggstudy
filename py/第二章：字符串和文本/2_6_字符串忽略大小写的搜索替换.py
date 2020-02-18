#########################################################################
# File Name: 2_6_字符串忽略大小写的搜索替换.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Nov 12 09:42:28 2019
#########################################################################
#!/usr/bin/env python3

import re
# 忽略大小写
# 需要 在 使用re模块的时候 给这些操作提供 re.IGNORECASE标志函数：
text = 'UPPER PYTHON,lower python,Mixed Python,Mixed PyThon Again,Mixed pyThon again'
print(re.findall('python',text,flags = re.IGNORECASE))

fs = re.sub('python','snake',text,flags = re.IGNORECASE)
print(fs)

# 缺陷：替换字符没有自动跟随原始字符大小写保持一致
# 辅助函数：
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

ful = re.sub('python',matchcase('snake'),text,flags = re.IGNORECASE)
print(ful)
# matchcase('snake') 返回了一个回调函数（参数必须是match对象）
# sub() 函数除了接受替换字符串外，还能接受一个回调函数。
# re.IGNORECASE 参数 对于某些需要大小写替换的Unicode匹配可能还不够。 -->2_10

