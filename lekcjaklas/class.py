class Pets:
    dogs =[]

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


class Dog:
    species = 'mammal'

    def __init__(self, name, age, walk):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.spacer = True

    def description(self):
        return "{} is {} years ond".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking".format(self.name)


def get_biggest_number(*args):
    return max(*args)


philo = Dog('Philo', 5, True)
mikey = Dog('Mikey', 4, False)
will = Dog('Will', 7, False)
print("{} is {} and has {}".format(philo.name, philo.age, mikey.name))
if philo.species == 'mammal':
    print("hes a mummal")
print("the oldres in the pack is {}".format(get_biggest_number(will.age, philo.age, mikey.age)))

print(mikey.description())
print(mikey.speak("gruf"))


class Terier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Cartoon(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


my_dogs = [
    Terier('Jack', 5, True),
    Terier("Jo", 4, True),
    Cartoon('Pinkey', 2, False)
]
my_pets = Pets(my_dogs)

for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}".format(dog.name, dog.age))

glodny = False

for dog in my_pets.dogs:
    if dog.is_hungry:
        glodny = True
if glodny:
    print('my dogs are hungry')
else:
    print('they are stacked full')

my_pets.walk()
