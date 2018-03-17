a = int(input())
b = (a % 10)
c = (a // 100)
e = a - (b + (c*100))
d = (e // 10)
g = b + c + d

print(g)
