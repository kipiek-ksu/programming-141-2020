"""Лабораторная работа 6
Толочный Виталий 141
Описати функцію IsPowerN (K, N) логічного типу, яка повертає True, якщо цілий
параметр K (> 0) є ступенем числа N (> 1), і False в іншому випадку. Дано число
N (> 1) і набір з 10 цілих позитивних чисел. За допомогою функції IsPowerN
знайти кількість степенів числа N в даному наборі."""

def IsPowerN (K, N):
    while(K % N == 0):
        K = K / N
    if K == 1:
        return True
    return False

N = int(input("Введите N: "))
x = 0
l1 = [int(K) for K in input("Введите K: ").split()]
for K in l1:
    if(IsPowerN(K,N)):
        x += 1
print(x)
