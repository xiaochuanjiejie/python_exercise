#coding: utf-8

import sys
import os
print globals()
print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))
print '------'
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
sys.path.append('/Users/zj/PycharmProjects')
from package2.brother2 import testfoo2
print testfoo2.foo()
# import package2
# print package2.brother2.testfoo2.foo()
# for i in sys.path:
#     print i

# if __name__ == "__main__" and __package__ is None:
#     from sys import path
#     from os.path import dirname as dir
#
#     path.append(dir(path[0]))
#     print path[0]
#     print dir(path[0])



