a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c
if a == 0:
    x1 = -c / b
    print(x1)
else:
    x1 = '{0:.6f}'.format((-b + d ** 0.5) / (2 * a))
    x2 = '{0:.6f}'.format((-b - d ** 0.5) / (2 * a))
    if d > 0:
        print(x2, x1)
    else:
        if d == 0:
            print(x1)
        else:
            print()
