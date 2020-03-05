while True:
    petla = input('chcesz zagrac w gre?')
    if petla == 'nie':
        break
    if petla == 'tak':
        x = input('kamien papier nozyce?')
        y = input('kamien papier nozyce?')
        x1 = x.lower().replace(' ', '')
        x2 = y.lower().replace(' ', '')
        if x1 == x2:
            print('remis. Jeszcze raz?')
        elif x1 == 'kamien':
            if x2 == 'papier':
                print('x1 lose')
            if x2 == 'nozyce':
                print('x1 win')
        elif x1 == 'papier':
            if x2 == 'nozyce':
                print('x1 lose')
            if x2 == 'kamien':
                print('x1 win')
        elif x1 == 'nozyce':
            if x2 == 'kamien':
                print('x1 lose')
            if x2 == 'papier':
                print('x1 win')
