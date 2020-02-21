from math import fmod

def oddq(a):
    if fmod(a,2)==0:
        print('Число чётное')
    else:
        print('Число нечётное')


a=int(input('Введите число\n'))
oddq(a)
