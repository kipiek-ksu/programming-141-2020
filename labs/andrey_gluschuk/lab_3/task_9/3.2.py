"""
     Глущук Андрій 141
     Лабораторна робота №3
     Завдання 2
 9. Дано натуральне число. Знайдіть число десятків у його десяткового запису.
"""


n = int(input("Enter a number: "))

if n > 0:
    while n > 100:
        n %= 100
    n //= 10
    print("Number of tens: ", n)
else:
    print("Error. Enter a natural number.")
