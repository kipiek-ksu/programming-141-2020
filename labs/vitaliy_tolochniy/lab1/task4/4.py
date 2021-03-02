"""
13. Дані координати двох протилежних вершин прямокутника: (x1, y1), (x2, y2).
Сторони прямокутника паралельні до осів координат. Знайти периметр і
площу даного прямокутника.
"""

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

AB = abs(y2 - y1)
BC = abs(x2 - x1)
P = 2 *(AB + BC)
S = AB * BC
print('Perimeter = ', P, 'Square = ', S)
