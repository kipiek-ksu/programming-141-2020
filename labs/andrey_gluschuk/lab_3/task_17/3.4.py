"""
     Глущук Андрій 141
     Лабораторна робота №3
     Завдання 4
 17. Дано ціле число N (> 1). Знайти найменше ціле число K, при якому виконується нерівність 3K> N
"""


n = int(input("Enter a integer: "))

if n > 1:
    K = 1
    while 3 * K <= n:
        K += 1
    print(K)
else:
    print("Error. N > 1")
