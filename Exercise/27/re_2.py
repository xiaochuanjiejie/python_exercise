#coding: utf-8

import re

ss = re.search(r'\w*\s+\w*','Jake wolf,3123s')
print ss.group()