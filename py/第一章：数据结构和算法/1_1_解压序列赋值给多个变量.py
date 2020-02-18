#########################################################################
# File Name: 1_1_解压序列赋值给多个变量.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 17 20:37:48 2019
#########################################################################
#!/usr/bin/env python3

p = (4,5)
x,y = p
print(x,'\n',y)

data = [ 'ACME',50,91.1,(2012,12,21) ]
name,shares,price,date = data
print(name,shares,price,date)

name,shares,price,(year,month,day) = data
for item in (name,shares,price,year,month,day):
    print(item)

s = 'Hello'
a,b,c,d,e = s
for item in (a,b,c,d,e):
    print(item)

# 去掉一部分
_,shares,price,_ = data
print(shares,price)


