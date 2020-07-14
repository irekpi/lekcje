class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        prod, cust, prom = len(self.products), len(self.customers), len(self.promotions)

        if item > prod*cust*prom:
            raise StopIteration
        else:
            pos_products = item//(prom*cust)
            item = item % (prom*cust)

            pos_promotions = item // cust
            item = item % cust

            pos_customers = item

        return '{} - {} - {}'.format(self.products[pos_products],
                                     self.promotions[pos_promotions],
                                     self.customers[pos_customers])



products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

# for i in range(1,30):
#     print(combinations[i])

comb = iter(combinations)
print(next(comb))