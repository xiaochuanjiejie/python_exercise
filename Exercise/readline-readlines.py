#-*- coding: utf-8 -*-
__author__ = 'xujunchuan'
f = open('/tmp/ip2.txt','r')

# for line in f.readline():
#     print line
#     # break

while True:
    for line in f.readline():
        print line
    if not line:
        break