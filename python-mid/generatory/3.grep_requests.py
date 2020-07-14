import os, requests


def gen_get_list(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


def gen_get_file_lines(filename):
    try:
        if filename.endswith('.txt'):
            with open(filename, 'r') as file:
                for line in file.readlines():
                    yield line.replace('\n', '')
    except:
        print('error')


def check_website(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False


with open('pomoce/grep_request.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('pomoce/gerp_request2.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

dir_path = '/home/zik/nauka/lekcje/lekcje/python-mid/generatory/pomoce'


for file in gen_get_list(dir_path):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_website(line)))
