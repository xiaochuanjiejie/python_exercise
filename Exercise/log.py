#-*- coding: utf-8 -*-
__author__ = 'chuan'
'''
client: 106.38.216.11, server: api.letv.com, \n
request: "GET /mms/out/album/videos?id=10014326&cid \n
=11&platform=pc&relvideo=1&relalbum=1&vid=23941833&year=2015&month=11&callback= \n
jQuery1710905325190090824_1447209723744&_=1447209739781 HTTP/1.0
'''

import sys
import re

# parr = r'.*client:(.+?),server:(sarrs.go.letv.com),request: "GET(.+?)HTTP/1.0'
parr = r'sarrs.go.letv.com'
f1 = open('./error.log')
f2 = open('./result.log','w')
for line in f1:
    m = re.findall(r'client: (.+?), server: (.*), request: (.*) HTTP/1.1',line)
    # print m[0][2]
    for i in m:
        f2.writelines(m[0][0] + '\t')
        f2.writelines(m[0][1] + '\t')
        f2.writelines(m[0][2] + '\n')
    # break
f2.close()
f1.close()