a = list(map(int, input().split()))
b = [int(input()) for i in range(a[1])]

b.sort()
b.reverse()
x = 0

z = sum(b)
print()

#while b < a:
#    a[0] = a[0] - b[x]
#    x += 1

# print(a[1] - x - 1)
