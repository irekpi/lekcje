import os

path = r'/home/zik/nauka/lekcje/python-mid/zmienne_i_kod/text.txt'
# file = open(path, 'x').close()  # tworzenie pliku


def open_read_count(path):
    file = open(path, ).read()
    splited = file.split()
    words_count = len(splited)
    return words_count


if os.path.isfile(path):
    print('liczba slow w path', open_read_count(path))

#  to samo tylko logiczna metoda
re_logic = os.path.isfile(path) and print('{} slowa w pathu {}'.format((open_read_count(path)), path))

