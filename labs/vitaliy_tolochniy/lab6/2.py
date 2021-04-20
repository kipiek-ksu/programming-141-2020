"""Лабораторная работа 6
Толочный Виталий 141
Описати функцію SumRange (A, B) цілого типу, яка знаходить суму всіх цілих
чисел від A до B включно (A і B - цілі). Якщо A> B, то функція повертає 0. За
допомогою цієї функції знайти суми чисел від A до B і від B до C, якщо дано
числа A, B, C. """

def SumRange (A, B):
    if A > B:
        return 0
    s = 0
    for i in range(A, B+1):
        s += i
    return s

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

l1 = []
l1.append(SumRange(A,B))
l1.append(SumRange(B,C))
print(l1)
