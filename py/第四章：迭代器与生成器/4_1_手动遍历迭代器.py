#########################################################################
# File Name: 4_1_手动遍历迭代器.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Dec 24 16:01:29 2019
#########################################################################
#!/usr/bin/env python3

# 遍历一个可迭代对象中的左右元素，不使用for循环。
# 使用next()函数，并在代码中捕获StopIteration异常。
# 例如：手动获取一个文件的所有行
def manual_iter():
    with open('./4_1_exa.txt') as f:
        try:
            while True:
                line = next(f)
                print(line,end='')
        except StopIteration as si:
            pass

# 手动使用next函数迭代结尾会返回None
#with open('./4_1_exa.txt') as f:
#    while True:
#            line = next(f,None)
#            if line is None:
#                    break
#            print(line,end='')

# 大多数时候会使用for循环语句用来遍历一个可迭代对象，
# 但是偶尔需要对迭代做更加精确的控制
# 了解底层迭代机制。

def iter_test():

    items = [1,2,3]
    # get the iterator
    it = iter(items) # Invokes items.__iter__()
    # run the iterator
    next(it) # Invokes it.__next__()
    next(it)
    next(it)
    try:
        next(it)
    except StopIteration as si:
        print(si)
    # run this in interactive enviroment.

def run():
    manual_iter()
    iter_test()

if __name__ == '__main__':
    run()
