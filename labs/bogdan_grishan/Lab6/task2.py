"""Описати функцію RingS (R1, R2) дійсного типу, яка знаходить площу кільця,
укладеного між двома колами із загальним центром і радіусами R1 і R2 (R1 і R2
- дійсні, R1> R2). З її допомогою знайти площі трьох кілець, для яких дані
зовнішні і внутрішні радіуси. Скористатися формулою площі круга радіусу R:
S = π · R2
. Як значення π вважати рівним 3.14"""


def RingS(r1, r2):
    r1 = float(r1)
    r2 = float(r2)
    area = float
    if r1 < r2:
        area = (3.14 * (pow(r2, 2))) - (3.14 * (pow(r1, 2)))
    return area


r1 = float
r2 = float
for x in range(0, 3):
    r1 = input("Введите значение r1=")
    r2 = input("Введите значение r2=")
    result = RingS(r1, r2)
    if result != 0:
        print(result)
    else:
        print("r1>r2, первый радиус должен быть меньше чем второй. Попробуйте снова")
