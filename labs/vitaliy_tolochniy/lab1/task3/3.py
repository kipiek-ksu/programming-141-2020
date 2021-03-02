"""
9. Дано двозначне число. Знайти суму і добуток його цифр
"""

a = int(input('Enter a two-digit number: '))
b = a // 10
c = a % 10
S = b + c
D = b * c
print('Sum = ', S, 'Product = ', D)
