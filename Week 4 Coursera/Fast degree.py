a = float(input())
n = int(input())
c = 0


def fast(a, n, c):
    if n % 2 != 0:
        c = (a ** 2) ** (n / 2)
    else:
        c = (a * (a ** (n - 1)))
    return c


print(fast(a, n, c))
