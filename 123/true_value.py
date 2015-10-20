#-*- coding: utf-8 -*-
__author__ = 'chuan'

'''
真值表
'''


print 'p        q     p and q     p or q'
length = len('p        q     p and q     p or q')
print '-' * length

for p in [True,False]:
    for q in [True,False]:
        #关于-9可查看evernote中‘格式化字符串输出’标签页
        print '%-9s %-9s %-9s %-9s' % (p,q,(p and q),(p or q))