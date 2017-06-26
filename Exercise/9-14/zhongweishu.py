#-*- coding:utf-8 -*-
__author__ = 'xujunchuan'
import re
t_list = []
num = raw_input('input number: ')
t_list = re.split(',',num)
length = t_list.__len__()
print length
#python浮点数list排序(http://blog.csdn.net/pirage/article/details/9282717)
t_list.sort(cmp=lambda x,y: cmp(float(x), float(y)), reverse = False)
#3.0,2.1,18.9,13.5
if length % 2 == 0:
    a = t_list[length / 2 - 1]
    b = t_list[length / 2]
    zhongweishu = (float(a) + float(b)) / 2
    print zhongweishu
else:
    a = t_list[(length - 1) / 2]
    zhongweishu = a
    print zhongweishu