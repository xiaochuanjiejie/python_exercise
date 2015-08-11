__author__ = 'chuan'

a = {}
c = 1

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                print i,j,k
                a[c] = (i,j,k)
                c = c + 1
print a