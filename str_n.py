def str_n(s,n):
    if len(s)>n:
        print(s.upper())
    else:
        print(s)

s=str(input("Введите строку\n"))
n=float(input("Введите число\n"))
str_n(s,n)
