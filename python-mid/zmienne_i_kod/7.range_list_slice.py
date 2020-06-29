import urllib.request, requests

color_list = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']


def color_pick(list, count):
    new_list = list.copy()
    new_picks = new_list[:count]
    print(new_picks)
    return new_picks


color_pick(color_list, 5)


for i in range(1,len(color_list)+1):
    print(color_pick(color_list, i))

#  Todo wyciaganie wiersza
# url = r'https://nonsa.pl/wiki/Korporacja'
# file = requests.get(url).text
file = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja,' \
       'która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem ' \
       'realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do ' \
       'wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '

print(file[file.index('(')+1:file.index(')')])

# even = [n for n in numbers[:None if 412 not in numbers else numbers.index(412)] if not n % 2] sprytna metoda