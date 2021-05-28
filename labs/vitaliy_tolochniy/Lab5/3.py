
list1 = []
a = int(input("Вы хотите, чтобы ваша матрица была сгенерирована или вы сами ее введете? (Тип 0 или 1): "))
if a == 1:
    num = int(input("Введите количество строк в вашей матрице: "))
    for i in range(0, num):
        list1.append(module.InputList())
else:
    num = int(input("Введите количество строк в вашей матрице: "))
    n = int(input("Введите длину строк в своей матрице: "))
    for i in range(0, num):
        list1.append(module.RandInt(n))

S = 0
for i in range(0, num):
    for j in list1[i]:
        if int(j)%3 == 0:
            S+=int(j)
print(S)
S = 0

for j in range(0, len(list1)):
    if int(list1[j][2]) < 0:
        S+=int(list1[j][2])
print(S)
