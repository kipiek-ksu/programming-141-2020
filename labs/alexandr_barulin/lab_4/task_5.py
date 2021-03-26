"""
Дано список A, кількість елементів якого N. Сформувати новий список B того ж розміру за таким правилом:
елемент BK дорівнює середньому арифметичному елементів масиву A з номерами від 1 до к.
"""

from random import randint

N = 10
a = [randint(0, 20) for _ in range(N)]
summ = 0
res = []
for i, e in enumerate(a):
    summ += e
    res.append(f'{summ / (i + 1):.2f}')
print(a)
print(res)
