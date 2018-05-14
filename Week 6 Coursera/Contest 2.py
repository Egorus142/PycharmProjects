a = int(input())
people = [input().split() for _ in range(a)]

for i in sorted(people, key=lambda x: int(x[1]), reverse=True):
    print(i[0])
