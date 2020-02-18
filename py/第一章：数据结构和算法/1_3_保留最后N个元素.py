#########################################################################
# File Name: 1_3_保留最后N个元素.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Mon Oct 21 14:27:34 2019
#########################################################################
#!/usr/bin/env python3

from collections import deque
# 
def search(lines,pattern,history=5):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'./somefile.txt') as f:
        for line,prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline,end = "")
            print(line,end='')
            print('-' * 20)

q = deque() # 不设置maxlen，得到无限大的队列
q.append(1)
q.append(2)
q.append(3)
q.appendleft(4)# 在左边增加项
q.pop()
q.popleft()# 在左边删除

# 在队列两端插入 或 删除 元素 时间复杂度都是O(1)，而在列表开头插入或者删除元素的时间复杂度为O(N)
