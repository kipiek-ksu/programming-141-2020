"""
     Глущук Андрій 141
     Лабораторна робота №4
     Завдання 3
 9. Дано рядок, що містить принаймні один символ пробілу. Вивести підрядок, розташований між
першим і останнім пробілом початкового рядка. Якщо рядок містить тільки один пробіл, то вивести
порожний рядок.
"""

S = input("Enter string: ")

print(S[int(S.find(' ')): int(S.rfind(' '))])
