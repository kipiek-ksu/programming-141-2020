"""З множини чисел [1..n] виділити підмножину простих чисел виду k2+1."""
n = 45
s = set(range(n))  # создает множину от 0 до 44
# функция проверяющаяя простое число или нет
def zna(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
s = filter(zna, s)
s = filter(lambda x: ((x - 1) ** 0.5) % 1 == 0, s)
print(set(s))
