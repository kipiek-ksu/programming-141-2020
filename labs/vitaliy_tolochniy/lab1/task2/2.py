"""
5. Обчислити дробову частину середнього геометричного трьох заданих позитивних
чисел.
"""

a1 = float(input('Enter 1 number: '))
a2 = float(input('Enter 2 number: '))
a3 = float(input('Enter 3 number: '))

k = (a1 * a2 * a3) ** (1 / 3)

print('Geometric mean = ', k)
