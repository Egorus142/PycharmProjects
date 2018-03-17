a = float(input())
b = float(input())
h = float(input())

p = (a+b+h) / 2
s = (p * (p - a) * (p - b) * (p - h))**0.5

print('{0:.6f}'.format(s))
