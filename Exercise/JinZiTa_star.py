#-*- coding: utf-8 -*-
__author__ = 'chuan'
'''
    *
   ***
  *****
 *******
*********
'''

line = 1
while line < 6:
    i = 1
    while i < 6:
        value1 = 6 - i
        i += 1
        if value1 > line:
            print ' ',
        elif 1 < value1 <= line:
            print '*',
        else:
            print '*',
            j = 2
            while j < 6:
                if j > line:
                    print ' ',
                else:
                    print '*',
                j += 1
    print '\n'
    line += 1

print '两种解法'
i1 = 0
while i1 < 7:
    space1 = " " * 2 * (6 - i1)
    print space1,
    j1 = 1
    while j1 <= i1:
        print '*',
        j1 += 1
    k1 = 1
    while k1 < i1:
        print '*',
        k1 += 1
    print '\n'
    i1 += 1
    # if i1 > 6:
    #     i2 = 1
    #     while i2 < 6:
    #         space2 = ' ' * 2 * i2
    #         print space2,
    #         print '* ' * (2 * (6 - i2) - 1),
    #         print '\n'
    #         i2 += 1
            # j2 = 1
            # while j2 <= 6:
            #     print '*',
            #     j2 += 1
            # k2 = 1
            # while
            # i2 += 1