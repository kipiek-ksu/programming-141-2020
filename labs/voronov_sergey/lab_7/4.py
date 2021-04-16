"""Описати рекурсивну функцію Palindrome (S) логічного типу, яка повертає True,
якщо ціле S є паліндромом (Читається однаково зліва направо і справа наліво),
і False в іншому випадку. Оператор циклу в тілі функції не використовувати.
Вивести значення функції Palindrome для п'яти даних чисел"""

def is_mirror(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_mirror(s[1:-1])


print(is_mirror('121'))
print(is_mirror('233'))
print(is_mirror('222'))
print(is_mirror('999000999'))
print(is_mirror('123321'))
