#-*- coding: utf-8 -*-
__author__ = 'chuan'
'''
      1
     212
    32123
   4321234
  543212345
 65432123456
7654321234567
'''
# a = 1
# while a < 8:
#     i = 8
#     j = 1
#     while j < i:
#         value = i - j
#         j += 1
#         if value > a:
#             print ' ',
#         # else:
#         #     print value,
#         elif 1 < value <= a:
#             print value,
#         else:
#             print value,
#             value1 = 2
#             while value1 < 8:
#                 if value1 > a:
#                     print ' ',
#                 else:
#                     print value1,
#                 value1 += 1
#     a += 1
#     print '\n'
print '第二种解法'
i1 = 1
while i1 < 8:
    space1 = ' ' * (7 - i1)
    print space1,
    j1 = i1
    while j1 > 0:
        print j1,
        j1 -= 1
    j2 = 2
    while j2 <= i1:
        print j2,
        j2 += 1
    print '\n'
    i1 += 1