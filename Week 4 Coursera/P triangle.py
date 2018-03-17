x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())


def d(a, b, c, d):
    return (((a - c) ** 2 + (b - c) ** 2) ** 0.5)


rez = (d(x1, y1, x2, y2)) + (d(x2, y2, x3, y3)) + (d(x3, y3, x1, y1))

print(rez)
