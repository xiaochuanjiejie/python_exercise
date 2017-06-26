#-*- coding: utf-8 -*-

class MoneyFmt(object):
    #钱作为对象的属性：值，负号
    def __init__(self,value=0.0,flag='-'):
        self.mvalue = value
        self.flag = flag
    def dollarize(self):
        val = round(self.mvalue,2)
        strvalue = str(val)
        pos = strvalue.find('.')
        while (pos - 3) > 0:
            strvalue = strvalue[:pos-3] + ',' + strvalue[pos-3:]
            pos -= 3
        if strvalue.startswith('-'):
            return self.flag + '$' + strvalue[1:]
        else:
            return '$' + strvalue
    def __nonzero__(self):
        if self.mvalue == 0:
            return False
        else:
            return True
    #更新数值便于类的多次使用
    def update(self,newvalue=None):
        if newvalue is not None:
            self.mvalue = float(newvalue)
    def __str__(self):
        print '__str__'
        return self.dollarize()
    def __repr__(self):
        print '__repr__'
        return repr(self.mvalue)

d = MoneyFmt(-123123123.456)
print d
print "%r" % d
d.update(234234.123)
print d