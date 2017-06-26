#-*- coding:utf-8 -*-
__author__ = 'xujunchuan'
import re

word_list = []
word_dict = {}

with open('/tmp/word.txt','r') as f1, open('/tmp/gettysburg','w') as f2:
    for line in f1.readlines():
        # word_list.append(line.split(' '))
        word_list.append(re.split(',| |\.|\\n',line))
    # print word_list
    for item in word_list:
        for item_son in item:
            if item_son not in word_dict:
                word_dict[item_son] = 1
            else:
                word_dict[item_son] += 1
# print word_dict
    for key in word_dict:
        print key,word_dict[key]
        f2.write(key + ' ' + str(word_dict[key]) + '\n')