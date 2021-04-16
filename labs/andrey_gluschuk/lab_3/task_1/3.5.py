"""
     Глущук Андрій 141
     Лабораторна робота №3
     Завдання 5
 1. Підрахувати k - кількість цифр в десятковому запису цілого невідємного числа n.
"""


n = int(input("Enter a number N: "))
digits = 0

if n >= 0:
    while n:
        digits += 1
        n //= 10
    print("Amount of digits: ", digits)
else:
    print("Error. Enter a positive number N.")
