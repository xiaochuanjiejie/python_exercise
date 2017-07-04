#coding: utf-8

import re

sub_list = []
dos = {}.fromkeys(('com','com.cn','net','org','edu'),0)
sub_email = 'test@163.com'
sub_dos = '|'.join(dos.keys())

with open('/tmp/email.txt','r') as f1:
    for line in f1.readlines():
        sub_list.append(re.sub(r'([\w.-]+)@([\w]+).(%s)' % sub_dos,sub_email,line))

with open('/tmp/sub_test.txt','w') as f2:
    f2.writelines(sub_list)