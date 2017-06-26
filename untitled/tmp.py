#-*- coding: utf-8 -*-

import os
import sys

print globals()
print sys.path
print sys.path[0]                       # 展示当前代码所在目录:/Users/zj/PycharmProjects/untitled
print os.path.dirname(sys.path[0])      # 显示代码所在的父目录:/Users/zj/PycharmProjects
print os.path.abspath(__file__)         # 显示代码名称:/Users/zj/PycharmProjects/untitled/tmp.py
print os.path.dirname(os.path.abspath(__file__))    # 显示代码所在的父目录:/Users/zj/PycharmProjects