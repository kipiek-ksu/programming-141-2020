"""Описати рекурсивну функцію PowerN (X, N) дійсного типу, яка знаходить
значення N-го степеня числа X за формулами:
X 0 = 1,
X N = (X N / 2) 2 при парних N> 0,
X N = X · X N-1 при непарних N> 0,
X N = 1 / X -N при N <0
(X ? 0 - дійсне число, N - ціле; у формулі для парних N повинна
використовуватися операція цілочисельного ділення). За допомогою цієї функції
знайти значення X N для даного X при п'яти даних значення"""
import math
def PowerN(x,n):
    if n == 0:
        return 1
    if n > 0:
        return x * PowerN(x, n-1)
    return 1 / PowerN(x, -n)
n=int(input('Введите n:'))
x=int(input('Введите x:'))
for i in range (5):
    print(PowerN(x**n,n+i))
