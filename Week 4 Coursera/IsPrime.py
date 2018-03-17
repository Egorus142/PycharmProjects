import math
a = int(input())


def IsPrime(a):
    if a == 1 or a == 2:
        return 'YES'
    else:
        i = 2
        while a % i != 0:
            if i >= math.sqrt(a):
                return 'YES'
            i = i + 1
        return 'NO'


print(IsPrime(a))
