def combinations(products, promotions, customers):
    for i in products:
        for j in promotions:
            for k in customers:
                yield "{} - {} -{}".format(i, j, k)


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

combinations = combinations(products, promotions, customers)

for item in combinations:
    print(item)