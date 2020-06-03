import random


def passgen():
    x = int(input('jak dlugie ma byc haslo?'))
    y = input('jakie ma byc haslo? slabe/mocne')
    a = [1, 2, 3, 4]
    b = ['a', 'b', 'c', 'd']
    c = ['A', 'B', 'C', 'D']
    if y == "slabe":
        d = a + b
    else:
        d = a + b + c
    random.shuffle(d)
    e = "".join(map(str, d))
    print(e[:x])


passgen()

# malo mozliwosci randomu, brak powtarzania znakow
