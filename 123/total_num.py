#-*- coding: utf-8 -*-
__author__ = 'chuan'

'''
用程序判断一个数是否为完全数
完全数：一个数字等于它所有的真因子（除去自身以外的约数）之和
约数：整数a除以整数b（b！=0），除得的商为整数而且没有余数，就说a能被b整除，b能整除a。a称为b的倍数，b称为a的约数
eg:6=1+2+3
采用计数循环来写程序，一开始和sum值为0而后每逢能整除则将jishu值累加
'''

num = int(raw_input('input number: \n'))
#变量jishu即整数b（b！=0）
jishu = 1
sum = 0
while jishu < num:
    if num % jishu == 0:
        sum += jishu
    jishu += 1
if sum == num:
    print str(num) + '是完全数'
else:
    print str(num) + '不是完全数 '