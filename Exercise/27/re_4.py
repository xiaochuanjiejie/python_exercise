#coding: utf-8

'''
1.python中的标识符是区分大小写的。
2.标示符以字母或下划线开头，可包括字母，下划线和数字。
3.以下划线开头的标识符是有特殊意义的。
> 以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入；
> 以双下划线开头的（__foo）代表类的私有成员；
> 以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。
'''

import re

str1 = '_abc,abc,__abc__,1_abc,123'

ss = re.findall(r'\b[a-zA-Z_]\w+\b',str1)
print ss