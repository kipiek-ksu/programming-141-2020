"""
     Глущук Андрій 141
     Лабораторна робота №5
     Завдання 3
    10. Задано список, n=m (якщо треба згенерувати відповідний список). Написати програму, яка визначає чи є задана
квадратна матриця ортонормованою. Підказка: квадратна матриця є ортонормованою, якщо в ній скалярний добуток кожної
пари різних рядків дорівнює «0», а скалярний добуток кожного рядка на себе – «1».
"""


def isOrthogonal(a, m, n):
    if (m != n):
        return False

    transpon = [[0 for x in range(n)]
                for y in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            transpon[i][j] = a[j][i]

    prod = [[0 for x in range(n)]
            for y in range(n)]

    for i in range(0, n):
        for j in range(0, n):
            sum = 0
            for k in range(0, n):
                sum = sum + (a[i][k] *

                             a[j][k])
            prod[i][j] = sum

    for i in range(0, n):
        for j in range(0, n):
            if (i != j and prod[i][j] != 0):
                return False
            if (i == j and prod[i][j] != 1):
                return False

    return True


a = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

if (isOrthogonal(a, 3, 3)):
    print("Yes")
else:
    print("No")
