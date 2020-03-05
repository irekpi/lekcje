def schambles(x):
    y = x.split(' ')
    z = y[::-1]
    c = " ".join(z)
    print(c)


x = 'to jest testowy string ktory bedzie odwracany'
schambles(x)
