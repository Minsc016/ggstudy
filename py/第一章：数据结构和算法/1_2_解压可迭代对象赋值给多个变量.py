#########################################################################
# File Name: 1_2_解压可迭代对象赋值给多个变量.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 17 20:44:12 2019
#########################################################################
#!/usr/bin/env python3

# ************************************************************************ #
def drop_first_last(grades):
    first,*middle,last = grades
    return middle

a = [1,2,3,4,5,6,7,8,9,0]
print(a,drop_first_last(a))

record = ('Dave','dave@example.com','773-555-1212','847-555-1212')
name,email,*phone_numbers = record

print(record,'\n',name,'\n',email,'\n',phone_numbers)

# * 解压出去的是    列表   类型， 不管多少个，即使 是 0 个

*trailing,current = [10,8,7,1,9,5,10,3]
print("trailing:",trailing)
print('current:',current)

# 对可变 长元组
records = [
        ('foo',1,2),
        ('bar','wtf?'),
        ('foo',6,9)
        ]
def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
    else :
        pass


# 星号解压语法 在 字符串 操作 时 
line = 'nobody : * : -2 : -2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(':')
print('line:',line)
print(uname)
print(fields)
print(homedir)
print(sh)

# 丢弃 用 _______________ 或 ign
record = ('ACME',50,123.45,(12,18,2012))
name,*_,(*_,year) = record
print(record)
print(name)
print(year)
items = [1,10,7,4,5,9]
head,*tails = items
print(items,'\n',head,'\n',tails)

# 用来实现递归算法
def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head

print(sum(items))
