"""
Описати рекурсивну функцію DigitSum (K) цілого типу, яка знаходить суму цифр
цілого числа K, не використовуючи оператор циклу. За допомогою цієї функції
знайти суми чисел для п'яти даних цілих чисел."""

def DigitSum(N):
    if N > 10:
        return N % 10 + DigitSum(N // 10)
    return N

for i in range(0,5):
    print(DigitSum(int(input("Введите число"))))