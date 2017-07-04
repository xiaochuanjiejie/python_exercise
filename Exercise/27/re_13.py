#coding: utf-8

import re

def type(flag=''):

    '''
    input content:
    <type 'init'>
    <type 'float'>
    <type 'builtin_function_or_method'>
    '''
    if flag == 'h' or flag == 'help':
        print type.__doc__
    else:
        str1 = raw_input('input content(可输入h|help查看content): ')
        ss = re.search(r'<type\s+\'(\w+)\'>',str1)
        # ss = re.match("<type\s+'(\w+)'>", str1)
        print 'type is %s' % ss.group(1)

type()