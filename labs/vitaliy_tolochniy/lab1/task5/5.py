"""
17. Швидкість першого автомобіля V1 км/год, другого - V2 км/год, відстань між ними S км.
Визначити відстань між ними через T годин, якщо автомобілі спочатку рухаються назустріч один
одному. Дана відстань рівна модулю різниці початкової відстані і загального шляху, пройденого
автомобілями; загальний шлях = час · сумарна швидкість.
"""

V1 = float(input('Enter the speed of the 1st car: '))
V2 = float(input('Enter the speed of the 2st car: '))
S = float(input('Enter the initial distance between cars: '))
time = float(input('Enter the time: '))
Sz = time * (V1 + V2)
distance = abs(S - Sz)
print('The distance between the cars = ', distance)
