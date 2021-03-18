""" 4.(1)Дано ціле n>2. Вивести всі прості числа з діапазону [2,n] """
n = int(input('Введіть число n , яке має бути > 2: '))
lst = []
k = 0
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
print(lst)
