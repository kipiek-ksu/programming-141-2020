"""Описати функцію IsSquare (K) логічного типу, яка повертає True, якщо цілий
параметр K (> 0) є квадратом деякого цілого числа, і False в іншому випадку. З
її допомогою знайти кількість квадратів в наборі з 10 цілих позитивних чисел."""
import math
from math import sqrt


def is_square(k):
    return sqrt(k).is_integer()


for x in range(0, 10):
    k = float(input(""))
    print(is_square(k))
