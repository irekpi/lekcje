import random
count = 0
while True:
    petla = input('zagramy? y/n')
    count += 1
    if petla == 'y':
        y = input('podaj cyfre od 1 do 9')
        x = random.randint(1, 9)
        y = int(y)
        if x == y:
            print('trafiles')
        else:
            if x > y:
                print('Twoja liczba byla mniejsza', 'liczba prob:', count)
            else:
                print('liczba byla wieksza', 'liczba prob:', count)
    if petla == 'n':
        break
