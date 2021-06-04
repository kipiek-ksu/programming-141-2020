"""Описати функцію Exp1 (x, ε) дійсного типу (параметри x, ε - дійсні, ε> 0),
знаходить наближене значення функції exp (x):
exp (x) = 1 + x + x2
/ (2!) + x3
/ (3!) + ... + xn
/ (n!) + ...
(N! = 1 · 2 · ... · n). В сумі враховувати всі складові, більші за ε. За допомогою
Exp1 знайти наближене значення експоненти для даного x при шести даних ε"""


def exp1(x, e):
    s = float(0)
    c = float(1)
    n = int(1)
    while abs(c) < e:
        s += c
        n += 1
        c *= x * n / (n - 1)
    return s


for j in range(0, 6):
    x = float(input(""))
    e = float(input(""))
    print(exp1(x, e))
