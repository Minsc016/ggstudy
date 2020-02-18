#########################################################################
# File Name: 1_14_排序不支持原生比较的对象.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 24 10:45:17 2019
#########################################################################
#!/usr/bin/env python3

# 给sorted() 传入一个callable 对象 key 
class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

from random import randint
from operator import attrgetter
def sort_notcompare():
    randnums =[randint(1,100) for i in range(6)]
    users = [User(n) for n in randnums]
    print(users)
    print(sorted(users,key = lambda u:u.user_id))
    # 使用 operator 的 attrgetter 函数
    print(sorted(users,key = attrgetter('user_id')))


if __name__ == '__main__':
    sort_notcompare()
