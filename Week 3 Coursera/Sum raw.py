a = float(input())
c = 1
b = 0

while c <= a:
    b += (1 / c**2)
    c += 1

print('{0:.5f}'.format(b))
