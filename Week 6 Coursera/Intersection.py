import collections

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.extend(b)

print(*[item for item, count in collections.Counter(a).items() if count > 1])
