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

i = 0
counter_temp = []

r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=' + '65' + '&exp=json')
print(r)

if r.status_code == 200:
    universities: list = r.json()
    rectors = [{k: row[k] for k in ['university_name', 'university_director_post', 'university_director_fio']} for row
               in universities]

    for university in universities:
        counter_temp.append(universities[i]['education_type_name'])
        i += 1
    counter: dict = {a: counter_temp.count(a) for a in counter_temp}
    print(counter)

    headers = [
        'university_name',
        'university_address',
        'university_email',
        'university_site',
    ]
    contacts = [
        {**{k: row[k] for k in headers}, **{
            'google_address': 'https://www.google.com.ua/maps/search/' + '+'.join(
                row['university_name_en'].split()) + '/'}
         } for row in universities
    ]

    with open('contacts.csv', mode='w', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers + ['google_address'])
        writer.writeheader()
        writer.writerows(contacts)
    with open('rectors.csv', mode='w', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=rectors[0].keys())
        writer.writeheader()
        writer.writerows(rectors)
    with open('universities.csv', mode='w', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=universities.keys())
        writer.writeheader()
        writer.writerows(universities)
