"""
     Глущук Андрій 141
     Лабораторна робота №7
     Завдання 1-4
1. Получить ЗВО из указанного пользователем региона, и сохранить все данные о них (universities.csv). Если регион не из
списка возможных (в документации на странице) - сообщить в консоль о ошибке

2. О полученных ЗВО с типом Университет сохраните [Название, Должность, ФИО руководителя], отсортировав по ФИО (rectors.csv)

3*. Посчитайте статистику количества заведений по типу в регионе, сохраните её (types.csv), например
тип,количество
Университет,22
Колледж,30

4**. О всех полученных заведениях сформируйте файл с контактами (название, адресс, емейл, сайт)
Кроме адресса добавьте отдельным столбцом ссылку на гугл-карту, ведущую на поиск заведения, например
https://www.google.com.ua/maps/search/Kherson+marine+college+of+fishing+industry/
"""

import requests
import csv

temp_universities = None
region = input("Введите код региона (65 - Херсон): ")
select_function = None


def request(reg):
    r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=' + reg + '&exp=json')
    print(r)
    if r.status_code == 200:
        universities: list = r.json()
        with open('universities.csv', mode='w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=universities[0].keys())
            writer.writeheader()
            writer.writerows(universities)
        return universities


def rectors(universities):
    rectors = [{k: row[k] for k in ['university_name', 'university_director_post', 'university_director_fio']} for row
               in universities]
    with open('rectors.csv', mode='w', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=rectors[0].keys())
        writer.writeheader()
        writer.writerows(rectors)


def types(universities):
    i = 0
    counter = []
    for university in universities:
        counter.append(universities[i]['education_type_name'])
        i += 1
    counter: dict = {a: counter.count(a) for a in counter}  # не понял как считает count, нашел решение
    print(counter)  # выводит в консоль корректные значения
    """with open('types.csv', mode='w', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=counter.keys())
        writer.writeheader()
        writer.writerows(counter.items())"""  # пока что не понял как решить


def contacts(universities):
    contact = [{k: row[k] for k in ['university_name', 'university_address_u', 'university_email', 'university_site']}
               for row
               in universities]
    with open('contacts.csv', mode='w', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=contact[0].keys())
        writer.writeheader()
        writer.writerows(contact)


while select_function != 0:
    print("\n1 - Получить список ЗВО\n"
          "2 - Изменить регион\n"
          "3 - Создать файл rectors.csv\n"
          "4 - Посчитать статистику количества ЗВО по типу\n"
          "5 - Создать файл contacts.csv\n"
          "0 - Завершить работу программы\n")
    select_function = int(input("Введите номер функции: "))
    universities = request(region)
    if select_function == 1:
        request(region)
    elif select_function == 2:
        region = input("Введите код региона (65 - Херсон): ")
    elif select_function == 3:
        rectors(universities)
    elif select_function == 4:
        types(universities)
    elif select_function == 5:
        contacts(universities)
    else:
        print("Введён неверный номер функции!")

"""sorted_universities: list = []
i = 0
for university in universities:
    sorted_universities.append({'university_name_en': universities[i]["university_name_en"],
                                'university_email': universities[i]['university_email']})
    i += 1
"""  # пример альтернативы dict comprehensions
