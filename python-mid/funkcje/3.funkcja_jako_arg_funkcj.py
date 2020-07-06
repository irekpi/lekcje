def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


func_list = [double, root, negative, div2]
numb = [1, 2, 3, 4]


def generate_values(func, obj_list):
    for item in obj_list:
        print('Function {} for number {} is equal {}'.format(func.__name__, item, func(item)))


for item in func_list:
    generate_values(item, numb)