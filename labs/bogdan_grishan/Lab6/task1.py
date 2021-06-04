"""Описати функцію TrianglePS (a, P, S), яка обчислює по стороні a
рівностороннього трикутника його периметр P = 3 · a і площу S = a2
· (3) 1/2/4 (де
a - вхідний, P і S - вихідні параметри; всі параметри є дійсними). За допомогою
цієї функції знайти периметри і площі трьох рівносторонніх трикутників з даними
сторонами"""


def TringlePs(a):
    p = float(3 * a)
    s = float((((a ** 2) * 3 ** (1 / 2)) / 4))
    print("P=", p, "S=", s)


a = float(input("Введіть значення сторони першого трикутника"))
TringlePs(a)
b = float(input("Введіть значення сторони другого трикутника"))
TringlePs(b)
c = float(input("Введіть значення сторони третього трикутника"))
TringlePs(c)
