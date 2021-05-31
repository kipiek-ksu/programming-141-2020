"""Описати рекурсивну функцію Fact (N) дійсного типу, яка обчислює значення
факторіала
N! = 1 · 2 · ... · N
(N> 0 - параметр цілого типу). За допомогою цієї функції обчислити факторіали
п'яти даних чисел.
"""


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(factorial(4))

"""import requests
import csv

r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=65&exp=json')

universities: list = r.json()

with open('TEST.csv', mode='w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=universities[0].keys())
    writer.writeheader()
    writer.writerows(universities)"""
