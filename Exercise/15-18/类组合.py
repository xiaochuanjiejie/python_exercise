#-*- coding: utf-8 -*-

class Cpu(object):

    def __init__(self,product):
        self.cputype = product

    def __str__(self):
        return 'cpu型号： %s' % self.cputype


class Computer(Cpu):

    def __init__(self,product2):
        self.cpu = Cpu(product2)  # 包含CPu类的实例对象

    def __str__(self):
        return 'computer cpu type: %s' % self.cpu

    # def __init__(self,product):
    #     super(Computer,self).__init__(product)

    def __del__(self):
        print "Cpu by by!"

old_computer = Computer(123)
print old_computer
del old_computer