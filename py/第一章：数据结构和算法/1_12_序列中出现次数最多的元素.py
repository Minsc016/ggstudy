#########################################################################
# File Name: 1_12_序列中出现次数最多的元素.py
# Author: Crow
# mail:qnglsk@163.com
# Created Time: Thu Oct 24 09:58:06 2019
#########################################################################
#!/usr/bin/env python3

# collections.Counter 类
# most_common() 方法 直接给出答案

w = 'look into my eyes look into my eyes the eyes the eyes the eyes not around the eyes dont look around the eyes look into my eyes u r under arrest'
words = w.split()

from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3个词
top_three = word_counts.most_common(3)
print(top_three)

# Counter 对象接受 任意 由 可哈希 (hashable) 元素 构成的序列对象。 
# 在底层实现上，一个Counter对象就是一个字典，将元素映射到它出现的次数上。
# eg:
print("\r word_counts['not']:",word_counts['not'],'\r\n',"word_counts['eyes']:",word_counts['eyes'])


# 手动增加计数，可用简单加法：
mw = 'why are you not looking in my eyes'
morewords = mw.split()
for word in morewords:
    word_counts[word] += 1

print(" word_counts['eyes']:",word_counts['eyes'])

# 或者使用 update() 方法
word_counts.update(morewords)
print(" word_counts['eyes']:",word_counts['eyes'])

# Counter 结合数学运算
a = Counter(words)
b = Counter(morewords)
c = a+b
print(a,'\n',b,'\n',c)
d = a-b 
print(d)
