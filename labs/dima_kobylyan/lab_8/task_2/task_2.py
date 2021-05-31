"""З множини чисел [1..n] виділити підмножину складних чисел виду 6k+1, і
підмножину простих чисел виду 6k+1.
"""
n = 69
s = set(range(n))


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_prime2(n):
    return not is_prime(n)

s = filter(is_prime2, s)
s = filter(lambda x: (x - 1) % 6 == 0, s)

print(set(s))
