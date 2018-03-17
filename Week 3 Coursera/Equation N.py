import math
a = float(input())
b = float(input())
c = float(input())
x1 = x2 = 0
disc = b ** 2 - 4 * a * c
if disc < 0 or a == b == 0 and c != 0:
    print('')
elif a != 0 and disc == 0:
    x = - b / (2 * a)
    print(x)
elif a == 0:
    print(-c / b)
elif a != 0 and disc > 0:
    x1 = (-b + math.sqrt(disc)) / (2 * a)
    x2 = (-b - math.sqrt(disc)) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1, x2)
