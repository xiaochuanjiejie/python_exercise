__author__ = 'chuan'

class firstclass():
    def __init__(self,value):
        self.data = value
    def dispaly(self):
        print self.data

x = firstclass('king')
y = firstclass('3.1415926')

x.dispaly()
y.dispaly()