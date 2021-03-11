"""10. Дано рядки S, S1 і S2. Замінити в рядку S останнє входження рядка S1 на рядок S2."""

S = input('Введите S: ')
S1 = input('Введите S1: ')
S2 = input('Введите S2: ')

index = S.rfind(S1)
size = len(S1)
S = S[:index] + S2 + S[index + size:]
print(S)
