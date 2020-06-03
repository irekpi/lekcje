import urllib.request

data_dir = r'/home/zik/nauka/lekcje/python-mid/zmienne_i_kod/pomoce/'

pages = [
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'}, # zakomentowac jesli chce sie zeby przeszlo
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}
]

for item in pages:
    item['data_dir'] = data_dir + item['name'] + '.html'

    try:
        save = urllib.request.urlretrieve(item['url'], item['data_dir'])
    except:
        print('Podaj poprawne adresy stron {}'.format(item['name']))
        break

else:
    print('Pobieranie wykonane w pelni')
