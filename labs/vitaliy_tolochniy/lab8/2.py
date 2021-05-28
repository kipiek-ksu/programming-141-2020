"""Лабораторная работа 8
Толочный Виталий 141
Задача 9
З множини чисел [1..n] виділити підмножину простих чисел виду k2+1"""

N = int(input("Введите N: "))
A = {i for i in range(N)}
list1 = [i * i + 1 for i in range(N)]
print(A.intersection(list1))
