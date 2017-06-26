#-*- coding:utf-8 -*-
'''
以下两种情况的就是闰年:
1.  能被4整除而不能被100整除;
2.  能被400整除.
'''

from random import randint

def leap_year(year):
    if year < 1900 or year > 2100:
        print '超出了本次闰年取值范围'
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return year

years = []
for loop in range(20):
    years.append(randint(1900,2016))

print years,'\n',filter(leap_year,years)

#列表解析
print [year for year in [randint(1900,2016) for loop in range(20)] if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)]