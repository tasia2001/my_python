from random import randint
L=["гроза","начало","май","весна","гром"]
word = L[randint(0,len(L)-1)]
num = randint(0,len(word)-1)
letter=word[num]
print(word[:num]+"?"+word[(num+1):]+"\n")
lett=input("Введите букву\n")
if lett==word[num]:
    print("Победа!")
else:
    print("Увы! Попробуйте в другой раз.\n Слово: "+word)


