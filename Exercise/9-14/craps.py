#-*- coding:utf-8 -*-
__author__ = 'xujunchuan'
import random
t_list = []
#1:player win;0:player lose;2: loop
game_status = 2
attempt = 0
while game_status == 2:
    first  = random.randint(1,6)
    second = random.randint(1,6)
    t_list.append([first,second])
    sum1 = first + second
    if sum1 == 7 or sum1 == 11:
        game_status = 1
        attempt += 1
        print 'player win.'
        break
    if sum1 == 2 or sum1 == 3 or sum1 == 12:
        game_status = 0
        attempt += 1
        print 'player lose.'
        break
    if sum1 > 3 and sum1 < 11:
        attempt += 1
        test = True
        while test:
            attempt += 1
            first  = random.randint(1,6)
            second = random.randint(1,6)
            sum2 = first + second
            t_list.append([first,second])
            if sum2 == 7:
                game_status = 0
                test = False
                print 'player lose.'
            if sum2 == sum1:
                game_status = 1
                test = False
                print 'player win.'

print t_list
print 'Attempt: %s' % attempt