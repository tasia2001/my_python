import math
def f(x):
    if 0.2<=x<=0.9:
        print(math.sin(x))
    else:
        print(1)


a=float(input("Введите число\n"))
f(a)
        
