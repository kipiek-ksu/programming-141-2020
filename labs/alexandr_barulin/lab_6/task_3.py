import math
"""
Описати функцію IsPrime (N) логічного типу, яка повертає True, якщо цілий параметр N (> 1)
є простим числом, і False в іншому випадку (число, більше 1, називається простим, якщо воно
не має позитивних дільників, крім 1 і самого себе). Дано набір з 10 цілих чисел, більших 1.
За допомогою функції IsPrime знайти кількість простих чисел в даному наборі.
"""

def IsPrime(N):
    i = 1
    Temp = True
    while (i<N/2):
        i += 1
        if math.fmod(N,  i) == 0:
            I = N
            Temp = False
    return Temp
Res = 0
for i in range(0, 10):
    print('N :')
    N=int(input())
    if IsPrime(N):
        Res += 1
print(Res)