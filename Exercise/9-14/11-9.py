def average(num):
    numlist = range(num)
    return reduce((lambda x,y:x+y),numlist) / len(numlist)
print average(5)