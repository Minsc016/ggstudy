#########################################################################
# File Name: 5_5_文件不存在才能写入.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: 2020年02月20日 星期四 10时04分09秒
#########################################################################
#!/usr/bin/env python3

# 向 一个文件中写入数据，但是前提 必须是这个文件在文件系统上不存在。
# 不允许覆盖已存在的文件内容。

# 解决方案
# 可以在open()函数中使用 x模式 来代替 w模式 的方法来解决这个问题。
with open ('somefile','wt') as f:
    f.write('Hello\n')

try:
    with open('somefile','xt') as f:
        f.write('Suprise')
except FileExistsError as fee:
    print(fee)

# 如果文件是 二进制的 ，可以用 xb 代替 xt


# 不小心覆盖一个已存在文件----的完美解决方案。
import os
if not os.path.exists('somefile'):
    with open ('somefile','wt') as f:
        f.write('Hello \n')
else:
    print('File already exists')

###########################################################################################
# 使用 x模式 更加简单。 python3 才有，旧版Python和python的底层C函数是没有的。



