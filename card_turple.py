#!/usr/bin/env python3
import random

card_turple = ('wuzetian','yingzheng','gongben','libai','houyi')
package = []

while 1:
    choose = int(input('''
    money makes you feel strong!
    please choose the number:
    1,picking card
    2,check bag
    3.package handle
    4,leave
    '''))

## when 1
    if choose == 1:
        num = int(input('enter the number:'))
        for i in range(0,num):
            n=random.randint(0,4)
            print('you pick:{}'.format(card_turple[n]))
            package.append(card_turple[n])

        print('card in bag')
        print('____________')

    if choose ==2:
        if len(package) == 0:
            print('there is no hero,go picking')
            print('___________________________')
        else:
            for i in package:
                print(i)
            print('___________________________')

    if choose == 3:
        if len(package) == 0:
            print('no hero,go picking')
            print('__________________')
        else:
            package.sort()
            for i in package:
                    print(i)
            print('___________________')

    if choose == 4:
        break
