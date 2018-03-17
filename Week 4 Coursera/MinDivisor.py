import math
a = int(input())


def MinDivisor(a):
    if a == 1:
        return a
    else:
        i = 2
        while a % i != 0:
            if i >= math.sqrt(a):
                return a
            i = i + 1
        return i


print(MinDivisor(a))
