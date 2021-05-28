"""Лабораторная работа 8
Толочный Виталий 141
Задача 6
З множини чисел [1..n] виділити перетин підмножин - чисел виду 4k+1 і
5k+4."""

N = int(input("Введите N: "))
A = {i for i in range(N)}

list1 = [4 * i + 1 for i in range(N)]
list2 = [5 * i + 4 for i in range(N)]

print(A.intersection(list1))
print(A.intersection(list2))
