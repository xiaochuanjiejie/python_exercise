#-*- coding:utf-8 -*-
__author__ = 'xujunchuan'
import re

fd = file("/tmp/gettysburg.txt","r")
a = []
b = []
for line in fd.readlines():
    #去掉每行头尾空白
    line = line.strip()
    a = a + b
    # print type(line),type(re.split(',',line)),re.split(',',line)[0]
    b = re.split(',| ',line)
#去掉列表中的空字符
for nothing in a:
    if nothing == '' or nothing == '-':
        a.remove(nothing)
print '单词个数: %s' % len(a),type(a)
a_new = list(set(a))
print a_new
print '去重后单词个数: %s' % len(a_new)
for word in a_new:
    print '单词(区分大小写) %s 在文章中的出现次数是 %d' % (word,a.count(word))