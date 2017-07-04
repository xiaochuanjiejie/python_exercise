#coding: utf-8

from random import randrange,randint, choice
from string import lowercase
from sys import maxint
from time import ctime
from os import linesep

# print randint(5,10)   生成一个随机整数
doms = ('com','net','org')

with open('/tmp/email.txt','w') as f:
    for i in range(randint(5, 10)):
        # dtint = randint(0, maxint - 1)
        # dtstr = ctime(dtint)
        '''
        dtstr = ctime(dtint)
        ValueError: unconvertible time
        事例代码是由参考书提供的，理论上maxint获取的值没有问题，在ctime格式化会获得到相应的时间值，此处的报错本不应该发生。
        后来仔细查看ctime格式时间的范围限定在0~2^32。测试脚本位于CentOS7 64位系统，这样得到的maxint值为9223372036854775807，远大于2^32的值。
        dtint是由表达式 dtint = randrange(maxint)获取的，这样的dtint在很大概率上会得到大于2^32的值，超出了ctime的处理范围，所以就脚本一直在报错。
        '''
        dtint = randrange(2**32)
        dtstr = ctime(dtint)

        shorter = randint(4, 7)
        em = ''
        for j in range(shorter):
            em += choice(lowercase)

        longer = randint(shorter, 12)
        dn = ''
        for j in range(longer):
            dn += choice(lowercase)

        st = '%s::%s@%s.%s::%d-%d-%d' % (dtstr,em,dn,choice(doms),dtint,shorter,longer)
        st += linesep
        f.write(st)