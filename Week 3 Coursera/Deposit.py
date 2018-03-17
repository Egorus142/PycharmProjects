p = float(input()) / 100 + 1
x = float(input())
y = float(input()) / 100

y1 = float('{0:.2f}'.format(y))


a = x * p + y1 * p
b = int(a + y1 // 100 / 100)

c = ((a - b) * 100)

print(b, round(c))
