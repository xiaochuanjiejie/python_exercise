__author__ = 'chuan'

def changer(a,b):
    a = 1
    b[0] = 'spam'
    return a,b

X = 2
L = [1,2]
a,b = changer(X,L)
print (a,b)

print '....'
X = 2
L = [1,2]
changer(X,L[:])
print X
print L