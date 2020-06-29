import math

argument_list = []
results_list = []

for i in range(100):
    argument_list.append(i / 10)

for x in argument_list:
    results_list.append(abs(math.sin(x) * x ** 2))

print('min = {}  max = {}'.format(min(results_list), max(results_list)))


argument_list = []
results_list = []

for i in range(100):
    argument_list.append(i / 10)

for x in argument_list:
    results_list.append(abs(x ** 3 - x ** 0.5))

print('min = {}  max = {}'.format(min(results_list), max(results_list)))