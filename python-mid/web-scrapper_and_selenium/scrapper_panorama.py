from bs4 import BeautifulSoup
import requests
import urllib.request, json
import re
from pprint import pprint



def get_and_save_data(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        li_list = soup.find_all(class_='card company-item py-2 container my-2')

        for item in li_list:
            single_url_get = requests.get(item.find(class_='font-weight-bold mb-0').contents[1].get('href'))
            soup = BeautifulSoup(single_url_get.content, 'html.parser')
            text_all = soup.find_all(class_='pb-2 section-content')

            #  Jsonation
            script = str(soup.find('script', text=re.compile('var company =')).contents[0]).split('var company = ')[1].replace(';','')
            json_script = json.loads(script)

            # Collectin data
            name = json_script['name']
            city = json_script['location']['city']['name']
            zip_code = json_script['location']['zip']
            street = json_script['location']['street']['normalizedName'] + ' ' + json_script['location']['street']['number']
            desc = json_script['products']
            category = json_script['trade']['keywords']
            service = json_script['keywordsList']
            phone = json_script['contact']['phone']['formatted']
            email = json_script['contact']['email']


            # pprint(json_script)
            print(name)
            print(city)
            print(zip_code)
            print(street)
            print(desc)
            print(category)
            print(service)
            print(phone)
            print(email)
            print('---------------------')


for item in range(1, 100):
    url = 'https://panoramafirm.pl/weterynarz/firmy,' + str(item) + '.html'
    get_and_save_data(url)