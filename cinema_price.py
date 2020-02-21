def cinema(movie,day,time,num):
    d1=1
    d2=1
    
    if num>=20:
        d2=0.8
    if day=='завтра':
        d1=0.95
    if movie=='Паразиты':
        if time==12:
            print(250*d1*d2*num)
        elif time==16:
            print(350*d1*d2*num)
        elif time==20:
            print(450*d1*d2*num)
        else:
            print('Данные некорректны')
    elif movie=='1917':
        if time==10:
            print(250*d1*d2*num)
        elif time==13:
            print(350*d1*d2*num)
        elif time==16:
            print(350*d1*d2*num)
        else:
            print('Данные некорректны')
    elif movie=='Соник в кино':
        if time==10:
            print(350*d1*d2*num)
        elif time==14:
            print(450*d1*d2*num)
        elif time==18:
            print(450*d1*d2*num)
        else:
            print('Данные некорректны')
    else:
        print('Данные некорректны')
    


movie=input('Укажите фильм\n')
day=input('Укажите дату (сегодня/завтра)\n')
time=int(input('Укажите время\n'))
num=int(input('Укажите количество билетов\n'))
cinema(movie,day,time,num)
