# -*- coding: UTF-8 -*-
__author__ = 'chuan'
#利用正则匹配将文本中包含时间的行打印出来，使用到了re Module（re 模块使 Python 语言拥有全部的正则表达式功能）
import re

t_file = open('/Users/chuan/Documents/t1')
for line in t_file:
    # print line
    # print '********'
    #模糊匹配
    # matchobj = re.match(r'(.*):(.*):(.*)',line,re.M)
    #精确匹配，可考虑使用time模块的strptime()
    matchobj = re.match(r'(.*):(.*):[0-9]{2}',line,re.M)
    if matchobj:
        print 'Match OBJ: ',matchobj.group()
        print 'Match OBJ: ',matchobj.group(1)
        print 'Match OBJ: ',matchobj.group(2)
        # print 'Match OBJ: ',matchobj.group(3)
t_file.close()