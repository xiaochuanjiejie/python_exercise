__author__ = 'xujunchuan'
import re

def getip(log):
    return re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',log)
f = open('/tmp/ip.txt','r')
t_list = []
for line in f.readlines():
    ip = getip(line)
    t_list.append(''.join(ip))
    # break
print len(t_list),t_list
print list(set(t_list))