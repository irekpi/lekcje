banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
list = []
for item in range(len(banknotes_coins)):
    list.append(0)
print(list)
dict_denominations = dict(zip(banknotes_coins, list))
dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for key in dict_denominations:
    print('{} is in here {}'.format(key, dict_denominations[key]))