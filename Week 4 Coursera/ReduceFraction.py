import math

n = int(input())
m = int(input())


def reducefraction(n, m):
    k = math.gcd(n, m)
    p = int(n / k)
    q = int(m / k)
    print(p, q)


reducefraction(n, m)
