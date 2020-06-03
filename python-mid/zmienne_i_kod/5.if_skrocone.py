# task 1
price = 123
bonus = 23
bonus_granted = True
'''
dluga wersja 
if bonus_granted:
    price -= bonus

print(price)
'''
# krotka wersja
price -= bonus if bonus_granted else price
print(price)