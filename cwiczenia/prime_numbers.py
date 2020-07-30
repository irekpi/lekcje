def is_prime():
    n = int(input('Type int N number:'))
    x = 1
    list = []
    for item in range(2, n+1):
        x = x * (item - 1)
        if (x + 1) % item == 0:
            list.append(item)
    return list


if __name__ == '__main__':
    print(is_prime())


