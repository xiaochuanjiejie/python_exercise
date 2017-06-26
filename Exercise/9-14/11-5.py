__author__ = 'xujunchuan'

def sale(rate=0.2):
    price = float(raw_input('Please input price: '))
    print 'tax is %10.2f' % round(price*rate,2)

sale()