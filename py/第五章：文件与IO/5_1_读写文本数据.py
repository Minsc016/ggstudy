#########################################################################
# File Name: 5_1_读写文本数据.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Jan 17 10:12:33 2020
#########################################################################
#!/usr/bin/env python3

# 读写各种不同编码的文本数据，比如ASCII,UTF-8，UTF-16编码等。

# 使用rt 模式的open() 函数读取文本文件：
# Read the entire file as a single string
with open('somefile.txt','rt') as f:
    data = f.read()

# Iterable over the lines of the file
with open('somefile.txt','rt') as f:
    for line in f:
        #process line
        pass

# 为了写入一个文件，使用带有wt模式的open() 函数，如果文件之前存在内容则清除并覆盖。
# Write chunks of test data
text1,text2 = 'hello','kitty'
with open('somefile.txt','wt') as f:
    f.write(text1)
    f.write(text2)

# Redirected print statement
line1,line2 = text1,text2
with open('somefile.txt1','wt') as f:
    print(line1,file=f)
    print(line2,file=f)

# 如果是在已存在的文件中添加内容，使用at的open() 函数
# 文件读写默认使用 系统编码 ， 可以通过调用sys.getdefaultencoding() 来得到。
# 在大多数机器上都是utf-8编码，如果已知要读写的文本是其他编码方式，
# 那么可以通过传递一个可选的encoding 参数给open() 函数。
with open('somefile.txt','rt',encoding='latin-1') as f:
    pass

# Python 支持非常多的文本编码。
# 常见编码： ascii,latin-1,utf-8,utf-16.
# 在web 应用程序中通常都是用utf-8,
# ascii对应从U+0000到U+007F范围内的7位字符
# latin-1是字节0-255 到U+0000至U+00FF范围内Unicode字符的直接映射。
# 当读取一个未知编码的文本时使用latin-1编码永远不会产生编码错误。
# 使用latin-1编码读取一个文件的时候也许不能产生完全正确的文本编码数据，但它能从中提取出足够多的有用数据。
# 同时，如果之后将数据回写回去，原先的数据还会保留。


# 读写文本文件一般来讲比较简单。注意几点：
# 1.with 语句给被使用的文件创建了一个上下文环境，但with控制结束时，文本会自动关闭。可以不使用with语句，但必须手动关闭文件。
f = open('somefile.txt','rt')
data = f.read()
f.close

# 2.换行符的识别问题。在Unix 和 Windows 中是不一样的。（\n 和 \r\n）
#  默认情况下，Python 会以统一模式处理换行符。
# 在这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个\n字符。
# 类似的，在输出时 会将换行符转换为系统默认的换行符。
# 如果不使用默认的处理方式，可以给open()函数传入参数newline='',
# Read with disabled newline translation
with open('somefile.txt','rt',newline='') as f:
    pass

# 在Unix 上读取Windows上的文本文件，hello.txt
# Newlines translation enabled (the default)
with open('hello.txt','rt') as f:
    print(f.read())

# Newline translation disabled
with open('hello.txt','rt',newline='') as g:
    print(g.read())


# 3.文本文件中可能出现的编码错误
f = open('somefile.txt','rt',encoding='ascii')
f.read()
# Traceback (most recent call last):
#    File "<stdin>",line 1,in <module>
#    File "/usr/local/lib/python3.3/encodings/ascii.py",line 26,in decode
#        return codecs.ascii_decode(input,self.errors)[0]
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position
# 12: ordinal not in range(128)
f.close()

# 如果报错，表示读取文本时指定的编码不正确。
# 仔细阅读说明。
# 修改编码依然错误，可以给open函数传递一个可选的error参数来处理。
# Replace bad chars with Unicode U+fffd replacement char
f = open('somefile.txt','rt',encoding='ascii',errors='replace')
print(f.read())
# Ignore bad chars entirely
g = open('somefile.txt','rt',encoding='ascii',errors='ignore')
print(g.read())
f.close()
g.close()
# 尽量避免经常使用errors参数来处理编码错误。
# 默认utf-8
