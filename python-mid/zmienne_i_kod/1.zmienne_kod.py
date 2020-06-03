# task 1
# inicjowanie zmiennych o tej samej wartosci w jednej linii
a = b = c = 10
print([(id(x), 'num {}'.format(x)) for x in (a, b, c)])

a = b = c = 20
print([(id(x), 'num {}'.format(x)) for x in (a, b, c)])

a = b = c = [1, 2, 3]
print([(id(x), x) for x in (a, b, c)])  # to samo ID

new = 4
a.append(new)
# zmiana id nastepuje u wszystkich bo to ta sama lokalizacja, dodanie 4 jako nowego elemntu tez
print([(id(x), x) for x in (a, b, c)])

# task 2
x = 10
y = 10
print(id(x), id(y))  # opytmalizator pythona nadaje to samo id

y = y + 1 - 1
print(id(x), id(y))  # opytmalizator pythona nadaje to samo id bo to proste dzialanie

y = y - 1231231231123123 + 1231231231123123
print(id(x), id(y))  # inne id bo dzialanie jest juz powazniejsze
