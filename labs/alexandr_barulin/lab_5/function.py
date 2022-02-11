import random

"""
Розробіть функції для здійснення наступних операцій зі списками:
1. Введення списку;
2. Заповнення списку випадковими числами;
3. Виведення списку;
4. Пошук елементу за значенням;
5. Пошук максимального елементу;
6. Сортування списку за зростанням (спаданням);
7. Пошук середнього арифметичного;
"""


def enter_list():
    a = input().split()
    print(a)
    return a


def out():
    print(enter_list())
    return enter_list


def random_list():
    x = 5
    mas = []
    for i in range(x):
        mas.append(random.randint(0, 10))
    print(mas)
    return mas


def search():
    temp = input().split()
    x = input()
    if temp.index(x):
        print(x, 'is list')
    return x


def max_element():
    print('max=', max(enter_list))
    return max


def sort():
    a = enter_list()
    print(sorted(a), sorted(a, reverse=True))
    return a


def average():
    a = enter_list()
    a = [x for x in map(int, a)]
    print("Average = " + str(sum(a) / len(a)))
    return a
