import math

n = int(input())
m = int(input())


def reducefraction(n, m):
    k = math.gcd(n, m)
    p = int(n / k)
    q = int(m / k)
    return p, q


(p, q) = reducefraction(n, m)
print(p, q)
