import random


def random_with_sum(number_of_values, asserted_sum):
    trial = 0
    numbers = list(range(number_of_values))

    while True:
        trial += 1
        for i in range(number_of_values):
            numbers[i] = random.randint(1, 101)

        if sum(numbers) == asserted_sum:
            yield ((trial, numbers))
            trial = 0


for item in range(10):
    (which_trial, number_tuple) = next(random_with_sum(3, 50))
    print('On {} we got {} which is total of asserted numbers {}'.format(which_trial, number_tuple, sum(number_tuple)))
