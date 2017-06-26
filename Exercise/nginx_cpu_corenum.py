#-*- coding: utf-8 -*-



for i in range(0,40):
    a = '0000000000000000000000000000000000000000'
    # print i,'***'
    list_a = list(a)
    list_a[i] = '1'
    print list_a
    s = ''.join(list_a)
    # print s
