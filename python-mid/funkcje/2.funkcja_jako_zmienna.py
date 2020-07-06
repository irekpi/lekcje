def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8
trans = [double, root, div2, negative]
trans2 = [root, root, div2, double]
value = number
for item in trans:
    value = item(value)
    print('{}: temporal result is {}'.format(item.__name__, item(number)))

number = 10
value = number
for item in trans2:
    value = item(value)
    print('{}: temporal result is {}'.format(item.__name__, item(number)))