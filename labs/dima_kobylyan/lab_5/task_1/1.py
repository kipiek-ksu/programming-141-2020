import random

"""Розробіть функції для здійснення наступних операцій зі списками:
1. Введення списку;
2. Заповня списку випадковими числами;
3. Виведення списку;
4. Пошук елементу за значенням;
5. Пошук  максимального елементу;
6. Сортування списку за зростанням (спаданням);
7. Пошук середнього арифметичного;"""


def vvedenya_list():
    lst = [2, 34, 5, 42, 24, 5, 8, 22, 65]
    return lst


def vuvod_rand():
    lst2 = [random.randint(1, 10, ) for i in range(10)]
    return lst2


r = vvedenya_list()
s = vuvod_rand()


def vuvod(tf: list):
    return vuvod(r)


def sort(ad: list):
    return ad.sort


def max(ma: list):
    return max(s)


def mean(number: list):
    return float(sum(number)) / max(len(number), 1)
