A = list(map(int, input().split()))

mindex = A.index(min(A))
maxdex = A.index(max(A))

minA = min(A)
maxA = max(A)

A.remove(minA)
A.insert(maxdex, minA)
A.remove(maxA)
A.insert(mindex, maxA)

print(*A)
