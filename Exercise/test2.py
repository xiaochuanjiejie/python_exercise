__author__ = 'xujunchuan'

f = open('/tmp/ip','r')
result = list()
for line in open('/tmp/ip'):
    print line,'$$$'
    line = f.readline()
    print line,'%%%'