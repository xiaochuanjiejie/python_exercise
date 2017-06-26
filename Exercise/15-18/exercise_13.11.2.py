#-*- coding: utf-8 -*-

class Item(object):
    #商品的属性：商品名，价格
    def __init__(self,product,price):
        self.product = product
        self.price = price
    def __str__(self):
        return '%s, %.2f' % (self.product,self.price)

class Cart(object):
    #购物车的属性：购物车命名，内容包括商品名、数量
    def __init__(self,product,price,name):
        self.name = name
        self.goods = Item(product,price)
        self.cartlist = {}
    def showcart(self):
        if self.cartlist:
            for item in self.cartlist:
                print self.name,':',item,'..',self.cartlist[item]
        else:
            print '购物车是空的，请选择商品'
    def acart(self,count=1):
        if self.goods not in self.cartlist:
            self.cartlist[self.goods] = count
        else:
            self.cartlist[self.goods] += count
    def dcart(self,count=1):
        if (self.goods in self.cartlist) and self.cartlist[self.goods] >= count:
            self.cartlist[self.goods] -= count
        if self.cartlist[self.goods] == 0:
            self.cartlist.pop(self.goods)

class User(object):
    #用户属性：用户名、对应的购物车
    def __init__(self,name):
        self.name = name
        self.userdb = []
    def showuser(self):
        print self.name,self.userdb
    def appendcart(self,cart):
        self.userdb.append(cart.name)
    def delcart(self,cart):
        self.userdb.remove(cart.name)

if __name__ == '__main__':
   c1 = Cart('tv',3000,'cart1')
   c1.acart(1)
   c1.showcart()
   c2 = Cart('iphone',4000,'cart2')
   c2.acart(2)
   c2.showcart()
   u1 = User('tom')
   u1.appendcart(c1)
   u1.showuser()