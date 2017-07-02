#coding: utf-8

import re

str1 = '朝阳10001昌平12334顺义123877'
ss = re.findall(ur"([\u4e00-\u9fa5]+)(\d+)",str1.decode('utf-8'))
print ss
for i in ss:
    print i[0],':',i[1]

dict1 = dict(ss)
for key in dict1:
    print key.encode('utf-8') + ':' + dict1[key].encode('utf-8')