#coding: utf-8

'''
re.IGNORECASE 不区分大小写
re.DOTALL     允许符号.匹配\n换行符
'''

import re

str1 = 'sds Asdsd8 pqwe\n aasdsaduh8\n'

ss = re.search('a.*8',str1,re.IGNORECASE)
print ss.group()

ss1 = re.search('a.*8',str1,re.DOTALL)
print ss1.group()

str2 = 'sds Asdsd8 pqwe\n Aasdsaduh8\n'

ss2 = re.findall('A.*8',str2,re.DOTALL)     #贪婪会取最大匹配值
print ss2

ss3 = re.findall('A.*?8',str2,re.DOTALL)    #非贪婪取到合适的就OK，符号.代表任意字符（因re.DOTALL故也包含了\n），符号*代表0次或多次
                                            #符号?代表前面的组合0次或1次，所以就非贪婪了
print ss3

str3 = '<b>foo</b> and <i>so on</i>'
ss4 = re.findall('<(.*?)>',str3)
print ss4               #findall只显示括号里的内容
ss5 = re.search('<(.*?)>',str3)
print ss5.group()       #search还会显示括号两边的内容