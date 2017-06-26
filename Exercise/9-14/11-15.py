#-*- coding: utf-8 -*-

def backward(strtest):
    if strtest:
        print strtest[0],
        return backward(strtest[1:])
    print '\n'

def forward(strtest):
    if strtest:
        print strtest[-1],
        return forward(strtest[:-1])
    print '\n'

backward('qweasd')
forward('qweasd')