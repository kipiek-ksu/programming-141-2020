#Дані координати двох протилежних вершин прямокутника: (x1, y1), (x2, y2).
# Сторони прямокутника паралельні до осів координат. Знайти периметр і площу даного прямокутника.
#Барулін Олександр 141 група.

x1 = float(input("Веедите координаты точки Х1: "))
y1 = float(input("Веедите координаты точки Y1: "))
x2 = float(input("Веедите координаты точки Х2: "))
y2 = float(input("Веедите координаты точки Y2: "))

AB = (y2 - y1)
BC = (x2 - x1)
P = 2*(AB + BC)
S = AB * BC

print("Периметр даного прямоугольника равен: " + str(P))
print("Площадь даного прямоугольника равна: " + str(S))