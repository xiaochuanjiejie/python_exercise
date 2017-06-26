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
    def __init__(self,name):
        self.name = name
        self.cartlist = {}
    def showcart(self):
        if self.cartlist:
            for item in self.cartlist:
                print self.name,':',item,'..',self.cartlist[item]
        else:
            print '购物车是空的，请选择商品'
    def appendcart(self,item,count=1):
        if item not in self.cartlist:
            self.cartlist[item] = count
        else:
            self.cartlist[item] += count
    def delcart(self,item,count=1):
        #在购物车中且数量大于等于一，则减去输入count值
        if (item in self.cartlist) and self.cartlist[item] >= count:
            self.cartlist[item] -= count
        #再次判断，以防出现商品数量为零的情况
        if self.cartlist[item] == 0:
            self.cartlist.pop(item)

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
    i1 = Item('tv',3333.9)
    i2 = Item('iphone',6772.1233)
    print i1,i2
    ctest = Cart('carttest')
    ctest.showcart()
    c1 = Cart('cart1')
    c2 = Cart('cart2')
    c3 = Cart('cart3')
    c1.appendcart(i1,2)
    c2.appendcart(i1)
    c3.appendcart(i2,5)
    c1.showcart()
    c2.showcart()
    c3.showcart()
    c1.delcart(i1)
    c2.appendcart(i1,5)
    c1.showcart()
    c2.showcart()
    u1 = User('x')
    u2 = User('y')
    u1.appendcart(c1)
    u2.appendcart(c2)
    u1.showuser()
    u2.showuser()
    u1.appendcart(c3)
    u1.appendcart(c2)
    u1.showuser()
    u1.delcart(c2)
    u1.showuser()