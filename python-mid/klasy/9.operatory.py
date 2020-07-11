class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __str__(self):
        return 'Cake: {}\nKind: {}\nAdditives: {}'.format(self.name, self.kind, self.additives)

    def __iadd__(self, other):
        if type(other) is list:
            additives = self.additives
            additives.extend(other)
            return Cake(self.name, self.kind, self.taste, additives, self.filling)
        elif type(other) is str:
            additives = self.additives
            additives.append(other)
            return Cake(self.name, self.kind, self.taste, additives, self.filling)
        else:
            return 'Error: Type is not supported'


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
print(cake01)
cake01 += ['cos', 'platki']
print(cake01)
cake01 += 'cos2'
print(cake01)
cake01 += 2312
print(cake01)
