z = int(input('podaj liczbe'))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
for i in a:
    if i < z:
        x.append(i)
print(x)
