#########################################################################
# File Name: createphnum.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Tue Jan 14 11:41:02 2020
#########################################################################
#!/usr/bin/env python3

import random

def create_a_phone():
    # 第二位数字
    second = [3,4,5,7,8][random.randint(0,4)]

    # 第三位数字
    third = {3:random.randint(0,9),
            4:[5,7,9][random.randint(0,2)],
            5:[i for i in range(10) if i != 4][random.randint(0,8)],
            7:[i for i in range(10) if i not in [4,9]][random.randint(0,7)],
            8:random.randint(0,9),}[second]

    # 最后八位数字
    suffix = random.randint(9999999,100000000)

    # 拼接手机号
    return "1{}{}{}".format(second,third,suffix)

if __name__ == '__main__':
    print(create_a_phone())
