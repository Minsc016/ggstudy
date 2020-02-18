#########################################################################
# File Name: 2_19_实现一个简单的递归下降分析器.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Nov 22 17:33:24 2019
#########################################################################
#!/usr/bin/env python3

# 根据一组语法 解析 文本并 执行命令，
# 构造一个代表输入的抽象语法树。
#如果语法非常简单，可以自己写这个解析器，而不用框架。

#　根据特殊语法 解析 文本的问题。
# 首先 以 BNF 或者 EBNF 形式 指定一个标准语法，比如 一个简单数学表达式语法可能：
# 19BNF and 19EBNF

# 在 EBNF 中， 被包含在 {...}* 中的规则是可选的。
# * 代表 0 次 或 多次重复（跟正则表达式中意义一样）

# 如果你对 BNF 的工作机制还不是很明白的话，就把它当做是一组左右符号 可相互替换的规则。
# 一般来讲，解析的原理 就是你利用 BNF 完成多个替换和扩展以匹配输入文本和语法规则。
# 假设正在解析 3 + 4 * 5 的表达式，
# 先要通过使用 -->2_18 中的技术分解为 一组令牌流，结果是个令牌序列：
# NUM + NUM * NUM

# 在此基础上，解析动作 会 试着 去 通过替换操作匹配语法到 输入令牌
#expr 
#expr ::= term { (+|-) term }*
#expr ::= factor { (*|/) factor }* { (+|-) term }*
#expr ::= NUM { (*|/) factor }* { (+|-) term }*
#expr ::= NUM { (+|-) term }*
#expr ::= NUM + term { (+|-) term }*
#expr ::= NUM + factor { (*|/) factor }* { (+|-) term}*
#expr ::= NUM + NUM { (*|/) factor}* { (+|-) term }*
#expr ::= NUM + NUM * factor {(*|/) factor }* { (+|-) term }*
#expr ::= NUM + NUM * NUM {(*|/) factor }* { (+|-) term }*
#expr ::= NUM + NUM * NUM{ (+|-) term }*
#expr ::= NUM + NUM * NUM

# 解析步骤 原理： 查找输入 试着 匹配语法规则 。
# 第一个输入令牌 NUM，替换首先匹配这个部分。 匹配成功后进入下一个令牌 + 。
# 当已经确定不能匹配下一个令牌的时候，右边的部分（比如{ (*/) factor }*就会被清掉。
# 在一个成功的解析中，整个右边部分会完全展开来匹配输入令牌流。

# -*- encoding: utf-8 -*-
"""
Topic: 下降解析器
Desc:
"""
import re
import pdb
import collections

# Toek specification
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM,PLUS,MINUS,TIMES,DIVIDE,LPAREN,RPAREN,WS]))

# Tokenizer
Token = collections.namedtuple('Token',['type','value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match,None):
        tok = Token(m.lastgroup,m.group())
        if tok.type != 'WS':
            yield tok

# Parser
class ExpressionEvaluator:
    '''
    Implementation of a recursive descent parser.Each method implements a single grammar rule. Use the ._accept() method to test and accept the current lookahead token. Use the ._expent() method to exactly match and discard the next token on the input (or raise a SyntaxError if it doesn't match).
    '''
    def parse(self,text):
        self.tokens = generate_tokens(text)
        self.tok = None # last symbol consumed
        self.nexttok = None # next symbol tokenized
        self._advance() #Ｌｏａｄ　ｆｉｒｓｔ　ｌｏｏｋａｈｅａｄ　ｔｏｋｅｎ
        return self.expr()
    
    def _advance(self):
        'Advance one token ahead'
        self.tok,self.nexttok = self.nexttok,next(self.tokens,None)

    def _accept(self,toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False
    
    def _expect(self,toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('expected' + toktype)

    # Grammar rules follow
    def expr(self):
        "expression ::= term { ('+' | '-' ) term }*"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*' | '/') factor }*"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM|( expr )"
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


def descent_parser():
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2 + 3'))
    print(e.parse('2 + 3 * 4'))
    print(e.parse('2 + (3 + 4) * 5'))
    # 错误测试
    # print(e.parse('2 + (3 + * 4)'))

if __name__ == '__main__':
    descent_parser()




# 文本解析 是 一个很大的主题。 关于 语法、解析器----编译器书籍。
# 编写一个 递归下降解析器：：：：      
# 1.获得所有的语法规则
# 2.将其转换为一个函数或者方法
# expr ::= term { ('+' | '-' ) term }*
# term ::= tactor {('*' | '/') factor}*
# factor ::= '(' expr ')'
# | NUM

#-------->>>>>>>> 转换为：
class ExpressionEvaluator:
    def expr(self):
        pass
    def term(self):
        pass
    def factor(self):
        pass

# 每个方法要完成的任务很简单，它必须从左至右 遍历语法规则的每一部分。 处理每个令牌。
# 从某种意义上讲，方法的目的就是要么 处理完语法规则，要么产生一个语法错误。
# 为此，：：：：
#1.如果规则中的下个符号 是另外一个语法规则的名字（比如term或factor)，就简单的调用同名的方法即可。即“下降”。控制下降到另一个语法规则中去。有时候规则会调用已执行的方法（比如，在factor ::= '(' expr ')' 中对expr 的调用）。 即“递归”。
#2.如果规则中下一个符号是个特殊符号，比如（），就得 查找下一个令牌并确认是一个精确匹配。 如果不配过，就产生一个语法错误。 本节中_expect() 方法。
#3. 如果规则中下一个符号为一些可能的选择项（比如+或-），必须对每一种可能情况检查下一个令牌。至右当它匹配一个的时候才能继续。 这也是本节中 _accept() 方法的目的。 它相当于 _expect() 方法的弱化版本，因为如果一个匹配找到了它会继续。 但是如果没找到，它不会产生错误而是回滚（允许后续的检查继续进行）。
#4。对于有重复部分的规则（比如在规则表达式 ::= term { ('+' | '-') term }* 中），重复动作通过一个while 循环来实现。 循环主题会收集或处理所有的重复元素直到没有其他元素可以找到。
#5.一旦整个语法规则处理完成，每个方法会返回某种结果给调用者。这就是在解析过程中值是怎样累加的原理，比如，在表达式 求值程序中，返回值代表标傲世解析后的部分结果。 最后所有值会在最顶层的语法规则方法中合并起来。
#
#递归下降解析器 可以用来实现非常复杂的解析。
#比如，python 本身就是通过一个 递归下降解析器 去解释的。可以查看     Python源码文件 Grammar/Grammar 来研究下底层语法机制。
#通过手动方式 实现 一个解析器 其实 有很多 局限和不足。
#
#其中一个局限，就是它们不能被用于包含任何左递归的语法规则中。比如，
#item ::= items ',' item
#| item
#-->
#def items(self):
#    itemsval = self.items()
#    if itemsval and self._accept(','):
#        itemsval.append(self.item())
#    else:
#        itemsval = [ self.item() ]
#
#expr ::= factor { ('+' | '-' | '*' | '/' ) factor }*
#facotr ::= '(' expression ')' | NUM
## 这个语法不能察觉 标准四则运算 中 的运算符优先级 
# 分开使用“expr" 和 "term"" 规则可以让它 正确工作。

# 对于复杂的算法，最好  选择某个解析工具，比如 PyParsing 或者 PLY。
# 使用PLY 重写表达式求值程序的代码。

from ply.lex import lex
from ply.yacc import yacc

# Token list
tokens = ['NUM','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN']
# Ignored characters
t_ignore = ' \t\n'
# Token specifications (as regexs)
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Token processing functions
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handler
def t_error(t):
    print('Bad character :{!r}'.format(t.value[0]))
    t.skip(1)

# Build the laxer
laxer = lex()
# Grammar rules and handler functions
def p_expr(p):
    '''
    expr : expr PLUS term
        | expr MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expr_term(p):
    '''
    expr : term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : term TIMES factor
    | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]
def p_factor(p):
    '''
    factor : NUM
    '''
    p[0] = p[1]
def p_factor_group(p):
    '''
    factor : LPAREN expr RPAREN
    '''
    p[0] = p[2]

def p_error(p):
    print('Syntax error')
parser = yacc()

# 程序中 所有代码 都位于 一个比较高的层次。
# 只需 为 令牌写 正则表达式 和 规则匹配时的高阶处理函数即可。
# 实际的运行解析器，接受令牌等等底层动作已经被库函数实现了。
# 使用得到的解析对象的例子：
print(parser.parse('2'))
print(parser.parse('2+3'))
print(parser.parse('2+(3+4)*5'))

# 如果想在 变成过程 中 来点 挑战和刺激， 编写解析器 和 编译器 是个不错的选择。
# 再次，一本编辑器的书籍会包含很多底层的理论知识。
# Python 自己的 ast 模块 值得一看。
