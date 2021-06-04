"""Описати рекурсивну функцію IsPowerN (K,N) логічного типу, яка повертає True,
якщо цілий параметр K (> 0) є ступенем числа N (натуральне число), і False в
іншому випадку. З її допомогою знайти кількість степенів числа N в наборі з 10
цілих позитивних чисел."""

def IsPowerN(K,N):
    if K == 1:
        return True
    elif K % N != 0:
        return False
    return IsPowerN(K // N,N)

n = int(input("Введите N: "))
s = 0
l1 = []

for i in range(0,10):
    if IsPowerN(int(input("Введите число: ")),n):
        s += 1
print(s)