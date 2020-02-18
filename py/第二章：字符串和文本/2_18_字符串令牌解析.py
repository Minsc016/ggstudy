#########################################################################
# File Name: 2_18_字符串令牌解析.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Nov 22 09:48:14 2019
#########################################################################
#!/usr/bin/env python3

# 有一个字符串 ，要 从左至右 将其解析 为 一个    令牌流

# ：
text = 'foo = 23 + 42 * 10'
# 为了 令牌化字符串， 不仅需要匹配模式， 还得 指定模式的类型。 比如：
# 将字符串转换为序列对：
tokens = [('NAME','foo'),('EQ','='),('NUM','23'),('PLUS','+'),
        ('NUM','42'),('TIMES','*'),('NUM','10')]

# 为了 执行 这样的切分 ： 1.利用 命名捕获 组的正则表达式 来定义所有可能的令牌，包括空格：
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))

# 上面模式中， ?P<TOKENNAME> 用于给一个模式命名，供 后面使用。
# 2. 为了令牌花，使用 模式对象 很少被人知道的    scanner()  方法。
# 此方法会创建一个scanner对象，在此对象不断 调用 match() 方法会一步步的扫描目标文本 ，
# 每步一个 匹配。eg:

scanner = master_pat.scanner('foo = 42')
#print(scanner.match())
#print(_.lastgroup,_.group())
#
#print(scanner.match())
#print(_.lastgroup,_.group())
#
#print(scanner.match())
#print(_.lastgroup,_.group())
#
#print(scanner.match())
#pritn(_.lastgroup,_.group())
#
#print(scanner.match())
#pritn(_.lastgroup,_.group())
#
#print(scanner.match())

from collections import namedtuple
# 将上面代码 打包到生成器：
def generate_tokens(pat,text):
    Token = namedtuple('Token',['type','value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())

# Example use
for tok in generate_tokens(master_pat,'foo = 42'):
    print(tok)

    # Produces output

# 过滤令牌流，可以定义更多的生成器函数或者 使用一个生成器表达式。
# 比如，过滤 所有 空白令牌：：：：
tokens = (tok for tok in generate_tokens(master_pat,text)
        if tok.type != 'WS' )

for tok in tokens:
    print(tok)


# 通常 令牌化 是很多高级文本解析 与 处理 的第一步。
# 为了使用上面的扫描方法，重要几点；
# 1.必须确认 使用 正则表达式 指定了所有输入中可能出现的文本序列。
# 如果有任何 不可匹配的文本出现，扫描就会直接停止。
# 所以指定了空白字符

# 2.令牌的顺序也是有影响的。 re 模块会按照制定好的顺序去做匹配。
# 如果一个模式恰好是另一个更长模式的子字符串，那么需要确定长模式卸载签名。eg:
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE,LT,EQ])) # Correct
# master_pat = re.compile('|'.join([LT,LE,EQ])) # Incorrect

# 第二个模式是错的，因为它会将 文本 <=  匹配为令牌LT 紧跟着 EQ，而不是LE。

# 3.需要留意 子字符串 形式的模式。比如，假设有2中模式


PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat = re.compile('|'.join([PRINT,NAME]))

for tok in generate_tokens(master_pat,'printer'):
    print(tok)

# Outputs

# 更高阶的令牌化技术，  需要查看PyParsing 或者 PLY 包，调用PLY的例子在-->2_19.
