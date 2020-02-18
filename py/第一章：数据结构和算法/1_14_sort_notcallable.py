#########################################################################
# File Name: sort_notcallable.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 17 20:30:13 2019
#########################################################################
#!/usr/bin/env python3

# 排序 不支持 原生 比较 的对象
# 例如：
class User():
    def __init__(self,user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

class sort_notcompare():
    users = [ User(23),User(3),User(99) ]
    print(users)
    print(sorted(users,key = lambda u:u.user_id))
    # 使用operator 的 attrgetter代替Lambda
    from operator import attrgetter
    print(sorted(users,key = attrgetter('user_id')))
