#########################################################################
# File Name: 2_12_审查清理文本字符串.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Nov 14 11:46:12 2019
#########################################################################
#!/usr/bin/env python3

# 清理类似 带音符 的 字符。

# 文本清理问题 会涉及到 包括文本解析与数据处理 等一系列问题。
# 在非常简单的情形下，可能会选择字符串函数str.upper() 和 str.lower() 将文本转为标准格式。
# 使用str.replace() 或者 re.sub() 的简单替换操作 删除/改变 指定的字符序列。
# 使用 -->2_9 小节的 unicodedata.nomalize() 函数将 unicode文本标准化
# 进一步，消除整个区间上的字符 或者 去除变音符，使用 str.translate() 方法。
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# 第一步清理空白字符。  创建一个小的转换表格 然后使用 translate() 方法。
remap = {
        ord('\t') : ' ',
        ord('\f') : ' ',
        ord('\r') : None # Deleted
        }
a = s.translate(remap)
print(a)
# 空白字符 \t 和 \f 已经被重新映射到一个空格。回车字符 r 直接被删除。
# 以 这个表格 为基础进一步构建更大的表格。比如，删除所有的和音符。
import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD',a)
print(b)
print(b.translate(cmb_chrs))
# 通过使用 dict.fromkeys() 方法构造一个字典，每个Unicode 和音符 作为键，对应的值全部为None.
# 然后使用 unicodedata.normalize() 将原始输入 标准化 为 分解形式字符。
# 然后调用 translate 函数删除所有重音符。
# 同样技术 可以用来删除其他类型的字符（比如控制字符）

# eg:构造一个将所有 Unicode 数字字符映射到对应的ASCII字符上的表格：
digitmap = { c: ord('0') + unicodedata.digit(chr(c))
        for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd' }
len(digitmap)

#Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# 另一种清理文本的技术 涉及到 I/0 解码与编码函数。思路：先对文本做一些初步清理
# 然后结合encode() 或者 decode() 操作 来清楚 或 修改它。
a = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD',a)
bb = b.encode('ascii','ignore').decode('ascii')
print(bb)

# 标准化 操作 将 原来的 文本 分解为单独 和音符 ，
# ASCII 编码/解码 简单的丢弃掉 字符
# 此方法仅仅 只在 最后的目标就是 获取到文本对应 ASCII表示 的时候生效。

# 文本字符清理 主要问题 ：运行的性能。
# 代码越简单，运行越快。
# ----对于简单替换操作，str.replace() 方法通常是最快的，甚至在多次调用的时候。
# 清理空白字符：：：：
def clean_spaces(s):
    s = s.replace('\r','')
    s = s.replace(' ','')
    s = s.replace('\t',' ')
    s = s.replace('\f',' ')
    return s

# 比 translate() 和 正则表达式 都要快很多。
# ----对于 执行 任何复杂字符 对 字符重新映射或者删除操作的话，translate() 方法会非常快。
# 尝试不同方法 去 评估 性能。

# 类似技术 可 适用于 字节。 （替换、转换、正则表达式）
