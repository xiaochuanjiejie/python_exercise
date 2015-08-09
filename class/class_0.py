__author__ = 'chuan'

class firstclass():
    def setdata(self,value):
        self.data = value
    def dispaly(self):
        print self.data

x = firstclass()
y = firstclass()

x.setdata('king')
y.setdata('3.1415926')
x.dispaly()
y.dispaly()