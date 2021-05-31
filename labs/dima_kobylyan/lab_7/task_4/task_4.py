"""Описати рекурсивну функцію Palindrome (S) логічного типу, яка повертає True,
якщо ціле S є паліндромом (Читається однаково зліва направо і справа наліво),
і False в іншому випадку. Оператор циклу в тілі функції не використовувати.
Вивести значення функції Palindrome для п'яти даних чисел."""


def isPalindrome(s):
    length = len(s);
    if length <= 1:
        return True
    if s[0] != s[length - 1]:
        return False
    return isPalindrome(s[1:length - 1])
