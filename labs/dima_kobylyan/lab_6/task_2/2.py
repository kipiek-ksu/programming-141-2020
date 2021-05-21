
def is_sguare(k: int) -> bool:
    if (k**(1/2)%1) == 0:
        return True
    else:
        return False


k = int(input('Enter K: '))

print(is_sguare(k))
