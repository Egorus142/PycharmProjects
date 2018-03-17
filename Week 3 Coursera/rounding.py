from math import floor, ceil

a = float(input())
b = a - int(a)

if b < 0.5:
    print(floor(a))
else:
    print(ceil(a))
