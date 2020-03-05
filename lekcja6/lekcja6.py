x = input('podaj jakies slowo')
y = len(x)
z = []
c = x[::-1]
if x == c:
    print('to palindrom')
else:
    print('niestety nie jest to palindrom')
