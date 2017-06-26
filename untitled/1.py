#-*- coding: utf-8 -*-

class Usa(object):

    def __init__(self,startmoney,n_25=0,n_10=0,n_5=0,n_1=0):
        self.startmoney = int(startmoney * 100)

    def out(self):
        self.n_25 = self.startmoney / 25
        self.money = self.startmoney % 25

        self.n_10 = self.money / 10
        self.money = self.money % 10

        self.n_5 = self.money / 5
        self.money = self.money % 5

        self.n_1 = self.money / 1

        return '%s美元可兑换为: %s个25美分 + %s个10美分 + %s个5美分 + %s个1美分' % (self.startmoney,self.n_25,self.n_10,self.n_5,self.n_1)


p = Usa(0.13)
print p.out()