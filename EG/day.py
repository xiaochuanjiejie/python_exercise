# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import time

print time.time()

b = raw_input('输入日期，eg：20150102： ')
#换算开年首日的unix时间戳
a = b[0:4] + '0101'
i = time.strptime(a,'%Y%m%d')
o = int(time.mktime(i))
#计算输入日的unix时间戳
q = time.strptime(b,'%Y%m%d')
w = int(time.mktime(q))

print int((w - o)/24/60/60)



