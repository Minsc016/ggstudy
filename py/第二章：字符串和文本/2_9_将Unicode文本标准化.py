#########################################################################
# File Name: 2_9_将Unicode文本标准化.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Wed Nov 13 16:40:11 2019
#########################################################################
#!/usr/bin/env python3

# 处理Unicode字符串，需要确保所有字符在底层有相同的表示。
# 在Unicode中，某些字符能够用多个合法的编码表示。eg:
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1,'\t',s2)
print(s1==s2)
print(len(s1),'\t',len(s2))
# 此文本使用两种形式来表示，第一种使用整体字符（U+00F1），第二种使用拉丁字母n后面跟一个~
# 组合（U+0303)

# 在需要比较字符串的程序 中 使用字符的多种表示 会产生问题。 
# 为了修正，可以使用 unicodedata 模块 将文本标准化：
import unicodedata
t1 = unicodedata.normalize('NFC',s1)
t2 = unicodedata.normalize('NFC',s2)
print('-------')
print(t1,'\t',t2)
print(t1==t2)
print(len(t1),'\t',len(t2))
print(ascii(t1),'\t',ascii(t2))

t3 = unicodedata.normalize('NFD',s1)
t4 = unicodedata.normalize('NFD',s2)
print('-------')
print(t3,'\t',t4)
print(t3==t4)
print(ascii(t3),'\t',ascii(t4))
print(len(t3),'\t',len(t4))

# normalize() 第一个参数 指定字符串标准化的方式。    
# NFC表示字符应该是整体组成，如果可能的话使用单一编码。
# NFD表示字符应该分解为多个组合字符表示
# Python 同样支持扩展的标准化形式 NFKC 和 NFKD,
# 它们在处理某些字符的时候增加了额外的兼容特性。
s = '\ufb01' # A single character
print(s)
print(unicodedata.normalize('NFD',s))
# Notice how the combined letters are broken apart here
print(unicodedata.normalize('NFKD',s))
print(unicodedata.normalize('NFKC',s))

# 标准化对于 任何需要以 一致 的 方式处理 Unicode 文本的程序都是非常重要的，
# 当处理来自用户输入的字符串 而 很难去控制编码的时候尤其如此。

# 在清理和过滤文本的时候字符的标准化也是很重要的，
# 比如，想要 清除 一些文本上面的变音符的时候（可能是为了搜索和匹配）

print('去除变音符')
t = unicodedata.normalize('NFD',s1)
print(''.join(c for c in t if not unicodedata.combining(c)))



