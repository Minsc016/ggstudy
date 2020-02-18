#########################################################################
# File Name: 5_2_打印输出至文件中.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Fri Jan 17 10:48:22 2020
#########################################################################
#!/usr/bin/env python3

# 将print() 函数的输出重定向到一个文件中去。
# 在print() 函数中指定file 关键字参数，
with open('somefile.txt1','wt') as f:
    print('ajsdlfjsadflnasdfojsdalfjlasf',file = f) 

# 必须以文本模式打开，二进制模式会报错。
