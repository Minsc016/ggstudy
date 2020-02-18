#########################################################################
# File Name: 下载进度.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 17 10:25:19 2019
#########################################################################
#!/usr/bin/env python3

import time
import random
# set speed to random integer
speed = 0
download_size = 0
file_size = 1000
while True:
    speed = random.randint(13,125)
    download_size += speed
    time.sleep(1)
    # ++++
    download_size = file_size if download_size >= file_size else download_size
    speed = 0 if download_size >= file_size else speed
    print('\r','已下载:{: >4}M,当前速度:{: >4}M/s,进度:{:5.2f}%'.format(download_size,speed,download_size/file_size*100),end='',flush=True)
    if download_size == file_size:
        print('\n\rdownload completed.downloaded {0}M.'.format(download_size))
        break

