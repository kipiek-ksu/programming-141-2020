import math


def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


a = int(input("Enter A:"))
b = int(input("Enter B:"))
print(gcd(a, b))
