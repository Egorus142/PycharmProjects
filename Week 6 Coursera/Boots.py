a = int(input())
b = list(map(int, input().split()))

c = sorted(b)
d = []

for i in range(len(c)):
   if c[i] == a or c[i] >= a + 3 and (c[i] - c[i - 1]) >= 3:
      d.append(c[i])

print(len(d))

