import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
page = requests.get(url).text
dict_animals = {}
flag = 1
first_name = 'А'
english_alphabet = list('ZYXWVUTSRQPONMLKJIHGFEDCBAЁ')
print("А")
while flag:
    soup = BeautifulSoup(page, 'lxml')
    names = soup.find('div', class_='mw-category-columns').find_all('a')
    for name in names:
        name_text = name.text.strip()
        name_url = name.get('href')
        if name_text[0] != first_name:
            first_name = name_text[0]
        if name_text[0] == 'A':
            flag = 0
            break
        dict_animals[name_text[0]] = dict_animals.get(name_text[0], 0) + 1
        print(f'{name_text}: {name_url}')
    if flag == 0:
        print("Конец списка животных")
        break
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text.strip() == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text
for key in list(dict_animals.keys()):
    if key in english_alphabet:
        del dict_animals[key]
list1 = list(sorted(dict_animals.keys()))
for key in list1:
    print(f'{key} : {dict_animals[key]}')