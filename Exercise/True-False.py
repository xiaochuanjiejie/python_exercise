#-*- coding: utf-8 -*-
__author__ = 'chuan'
'''
在空 处填上True或False
p q         (not p) or q    (p and q) or q  (p or q) and p  (p or q) and (p and q)
True  True
True  False
False True
False False
'''

title = 'p        q   (not p) or q    (p and q) or q  (p or q) and p  (p or q) and (p and q)'
print title
print '*' * len(title)
for p in [True,False]:
    for q in [True,False]:
        print '%-6s %-6s' % (p,q),
        print '%-20s %-15s %-15s %-15s' % ((not p) or  q,(p and q) or q,(p or q) and p,(p or q) and (p and q))
        # ,(p and q) or q,(p or q) and p,(p or q) and (p and q)