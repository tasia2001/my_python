
def op(s):
    print(s.index('я'))
    print(s.count("у"))
    if not s.isalpha():
        print(s.upper())
    if len(s) > 4:
        print(s.lower())
    print(s.replace("У","О"))



s="У лукоморья 123 дуб зеленый 456"
op(s)

    
    
