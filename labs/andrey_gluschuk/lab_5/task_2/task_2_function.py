from random import randint

N = int(input("Enter the width of the square matrix: "))


def list_random():
    a = []
    for i in range(N):
        z = []
        for j in range(N):
            n = randint(1, 9)
            z.append(n)
        a.append(z)
    return a


lst = list_random()


def list_changetozero():
    for i in range(N):
        for j in range(N):
            if j < i:
                lst[i][j] = 0


def list_out():
    for i in range(N):
        for j in range(N):
            print("%3d" % lst[i][j], end='')
        print()
