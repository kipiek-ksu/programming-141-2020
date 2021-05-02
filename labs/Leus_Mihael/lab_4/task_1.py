"""
lab4_z1
"""

"""
Дано рядок. Вивести окремі слова, що входять до нього, розділені пробілами, впорядкованими за
алфавітом, в стовпчик
"""

s = str(input ("string = "))
def spl (a):
    return a.split(' ')
def ran(a: list):
    a.sort()
    return a
def stolb (b):
    for i in b:
        print(i)
print(stolb(ran(spl(s))))