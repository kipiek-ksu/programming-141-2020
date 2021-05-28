"""Лабораторная работа 8
Толочный Виталий 141
Задача 12
З множини чисел [1..n] виділити підмножину досконалих чисел (число
називається досконалим якщо воно дорівнює сумі своїх власних дільників,
наприклад 6=3+2+1)"""

def FindTrueOrFalse(N):
    lists = []
    for i in range(1,N // 2 + 1):
        if N % i == 0:
            lists.append(i)
    S = 0
    for i in lists:
        S += i
    return S == N

N = int(input("Введите N: "))
A = {i for i in range(N)}
A1 = set()
for i in A:
    if FindTrueOrFalse(i):
        A1.add(i)
print(A1)
