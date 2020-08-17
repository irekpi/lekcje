#####
# Appending to list over specific logger moves
#####


# sec correct verison
def minimumSteps(loggedMoves):
    collection = 0
    for item in loggedMoves:
        if item == '../':
            collection += 1
        elif item != './':
            collection -= 1
    return abs(collection)


loggedMoves = ['x/', 'y/', '../', 'z/', './']
quickest_v2 = minimumSteps(loggedMoves)


#####
# Collsion on index positions with speed defined on index values
#####
def collision(speed, pos):
    total_col = 0
    index_speed = speed[pos]

    for no_index, item in enumerate(speed):
        if item > index_speed and no_index < pos:
            total_col += 1
        if item < index_speed and no_index > pos:
            total_col += 1
    return total_col


speed = [6, 6, 1, 6, 3, 4, 6, 8]
pos = 2
x = collision(speed, pos)


#####
# Create MainClass, make it generic and create other class which inherits from Main
#####
class Car:
    def __init__(self, is_sedan, no_sits):
        self.is_sedan = is_sedan
        self.no_sits = no_sits

    def getIsSedan(self):
        if self.is_sedan:
            return 'Car is sedan'
        else:
            return 'This is not sedan'

    def getSeats(self):
        return 'Car has {} seats'.format(self.no_sits)

    def getMilage(self):
        return 'Milage of car is = {}'.format(self.milage)


auto = Car(False, 5)
print(auto.getIsSedan(), auto.getSeats())


class Honda(Car):
    def __init__(self, is_sedan, no_sits, milage):
        super(Honda, self).__init__(is_sedan, no_sits)
        self.milage = milage

    def getMilage(self):
        return 'Milage of car is = {}'.format(self.milage)


class WagonR(Car):
    def __init__(self, milage):
        self.milage = milage

    def getMilage(self):
        return 'Milage of car is = {}'.format(self.milage)


class Innovo(Car):
    def __init__(self, milage):
        self.milage = milage

    def getMilage(self):
        return 'Milage of car is = {}'.format(self.milage)


some_car = Car(True, 5)
some_car2 = Honda(True, 5, 50505)
print(some_car2.getSeats(), some_car2.getMilage())
