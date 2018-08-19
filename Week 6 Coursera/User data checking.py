a = list(map(int, input().split()))
b = [int(input()) for i in range(a[1])]

b.sort()
x = 0

while a[0] > 0:
    a[0] = a[0] - b[x]
    x += 1

print(x - 1)