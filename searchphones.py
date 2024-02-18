import requests
from bs4 import BeautifulSoup
import re


def cleaning_number(dirty_number):
    clean_number = dirty_number.strip().replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
    return clean_number


def search_phones(url):
    page = requests.get(url)
    phones = set()
    soup = BeautifulSoup(page.text, features="html.parser")
    text = soup.text
    for m in re.finditer(r'8|\+7', text):
        telephone = text[m.start():m.start()+18]
        telephone = re.sub('\D', '', telephone)
        telephone = telephone.replace('+7', '8')
        match = re.search(r'^((8|\+7)[\- ]?)?[\d\- ]{11}$', telephone.strip())
        if match:
            dirty_number = match[0]
            clean_number = cleaning_number(dirty_number)
            phones.add(clean_number)
    phone_list = list(phones)
    return phone_list


if __name__ == '__main__':
    address_list = []
    url_address_1 = "https://repetitors.info/"
    url_address_2 = "https://thebull.ru/"
    address_list.append(url_address_1)
    address_list.append(url_address_2)
    telephone_list = []
    for address in address_list:
        search_phones = search_phones(address)
        for search_phone in search_phones:
            telephone_list.append(search_phone)
    print(telephone_list)