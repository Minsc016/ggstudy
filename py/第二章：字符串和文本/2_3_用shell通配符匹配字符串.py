#########################################################################
# File Name: 2_3_用shell通配符匹配字符串.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Nov  5 10:11:17 2019
#########################################################################
#!/usr/bin/env python3

# 使用 Unix Shell 中常用的通配符，比如 *.py,Dat[0-9]*.csv 等 去匹配文字字符串
# fnmatch 模块 提供了两个函数 fnmatch() 和 fnmatchcase() 
# 用法
from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))
print(fnmatch('Dat45.csv','Dat[0-9]*'))

names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
print([name for name in names if fnmatch(name,'Dat*.csv')])


# fnmatch() 函数 使用 底层操作系统的大小敏感规则（不同系统不一样）
# On OS X(Mac)
print(fnmatch('foo.txt','*.TXT'))
# False
# ON Windows
print(fnmatch('foo.txt','*.TXT'))
# True
# fnmatchcase() ，使用 书写 的 大小写模式匹配
print(fnmatchcase('foo.txt','*.TXT'))

# 处理 非 文件名 的字符串时  
addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1030 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
        ]
# 列表推导
from fnmatch import fnmatchcase
print([addr for addr in addresses if fnmatchcase(addr,'* ST')])
print([addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9] *CLARK*')])

#　如果需要做　文件名的匹配　最好使用　ｇｌｏｂ　模块。见５＿１３
