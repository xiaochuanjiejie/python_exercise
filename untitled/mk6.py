#coding: utf-8

import sys
sys.path.append('/Users/zj/PycharmProjects')

from package2.brother2 import testfoo2
testfoo2.foo()

import package2.brother2.testfoo2
package2.brother2.testfoo2.foo()