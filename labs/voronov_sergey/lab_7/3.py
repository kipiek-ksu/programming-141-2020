"""Описати рекурсивну функцію GCD (A, B) цілого типу, яка знаходить найбільший
спільний дільник (НСД, greatest common divisor) двох цілих позитивних чисел A і
B, використовуючи алгоритм Евкліда:
НСД (A, B) = НСД (B, A mod B), B ? 0; НСД (A, 0) = A,
де «mod» позначає операцію взяття залишку від ділення. За допомогою цієї
функції знайти НСД (A, B), НCД (A, C), НCД (A, D), якщо дано числа A, B, C, D."""
def gcd(num1, num2):
    if num1 == 0:
        return num2
    return gcd(num2 % num1, num1)
print(gcd(num1 = 2, num2 = 10))

