# -*- coding: UTF-8 -*-
__author__ = 'chuan'

# for i in range(1,10):
#     for j in range(1,10):
#         a = i * j
#         print '%s x %s = %s' % (i,j,a)

#此方法效果更佳
for i in range(1,10):
     for j in range(1,i+1):
         print i,'*',j,'=',i*j,
     print ''