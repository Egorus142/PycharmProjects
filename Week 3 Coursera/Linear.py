a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
s1 = float(input())
s2 = float(input())

det = a1 * b2 - b1 * a2

detx = s1 * b2 - s2 * b1
dety = s2 * a1 - s1 * a2

vx = detx / det
vy = dety / det

print(vx, vy)
