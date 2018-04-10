n = int(input())

a = ('+___ ')
c = ('|__\\ ')
d = ('|    ')

print(a * n)
for number in range(1, n + 1):
    print('|', number, ' /', sep='', end=' ')
print()
print(c * n)
print(d * n)
