options = ['load data', 'export data', 'analyze&predict']
choice = 'x'


def display_options(list1):
    print(['{}. {}'.format((i+1), options[i]) for i in range(len(options))])
    choice = input('podaj wartosc ')
    return choice


while choice:

    choice = display_options(options)
    if choice != '':
        print('Cos zostalo podane, teraz sprawdzimy co')
        try:
            choice_num = int(choice)
            if choice_num > 0 and choice_num <= len(options):
                print('Wybrano:', options[choice_num-1])
            else:
                print('Zasieg wybierania to maksymalnie {}'.format(len(options)))
        except:
            print('Podano litere, wybierz jeszcze raz')
    else:
        print('Niestety nie dokonano wyboru')
        break
