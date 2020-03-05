x = int(input('podaj liczbe'))
y = int(input('podaj 2 liczbe'))
if x % 2 == 0:
    print('twoja liczba jest parzysta')
elif x % 3 == 0 and x % 2 == 0:
    print('twoja liczba jest parzysta i jest wielokrotnoscia liczby 4')
else:
    print('twoja liczba jest nieprzaysta')
if x % y == 0:
    print('twoja liczba jest tez podzielna na ', y)
