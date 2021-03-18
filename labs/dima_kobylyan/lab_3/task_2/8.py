"""Дано дійсне A та ціле число N (> 0). Вивести 1 – A + A2 – A3 + ... + (–1)NAN. """
n = int(input('Введить ціле N: '))
a = int(input('Введіть дійсне А: '))
sum_ = 0
for i in range(n):
    sum_ = sum_ + (-1) ** i * a ** i
print(i)