# -*- coding: UTF-8 -*-
__author__ = 'chuan'

class student:
    def __init__(self,name,score):
        self.__name  = name
        self.__score = score
    def print_score(self):
        return '[%s,%s]' % (self.__name,self.__score)

if __name__ == '__main__':
    bob = student('bob smith',90)
    tom = student('tom jake',80)
    #下面第一个显示输出，第二个不显示，因为没有把return值print出来
    print  bob.print_score()
    tom.print_score()
    print tom._student__name