"""
Користувач вводить з клавіатури числа в рядок до тих пір, поки не введе число 0.
На основі введених даних потрібно сформувати список, що складається з квадратів введених чисел.
"""
n = int(input("Веведите числа:"))

print(list(map(lambda x: int(x)**2, iter(input, "0"))))
