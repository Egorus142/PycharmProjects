a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c

x1 = '{0:.6f}'.format((-b + d ** 0.5) / (2 * a))
x2 = '{0:.6f}'.format((-b - d ** 0.5) / (2 * a))

if d > 0:
    print(2, x2, x1)
else:
    if d == 0:
        print(1, x1)
    else:
        print(0)
