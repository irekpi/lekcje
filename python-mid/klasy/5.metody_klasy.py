import pickle
import glob

class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, addictions, filling, gluten_free, text):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addicions = addictions
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if self.kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('Not cake and unable to sign on muffins')

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.addicions) > 0:
            print("Additives:")
            for a in self.addicions:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)

    def set_filling(self, filling_name):
        self.filling = filling_name
        return self.filling

    def add_additives(self, additives):
        self.addicions.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('no sign was added')

    def save_to_file(self, path):
        with open(path, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as file:
            new_cake = pickle.load(file)

        cls.bakery_offer.append(new_cake)
        return new_cake

    Text = property(__get_text, __set_text, None, 'it helps to tell if you can make sings on cake')

    @staticmethod
    def get_bakery_file(path):
        return glob.glob('*.bakery')

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy new olr')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', True, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', False, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, 'cake is life')

cake01.save_to_file('cake01.bakery')
cake02.save_to_file('cake02.bakery')

cake05 = Cake.read_from_file('cake01.bakery')
cake05.show_info()

print(Cake.get_bakery_file(''))
