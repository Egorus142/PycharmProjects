n = int(input())
nlist = list(map(int, input().split()))
x = int(input())
z = x

if nlist.count(x) > 0:
    print(x)
else:
    while nlist.count(x) == 0 and nlist.count(z) == 0:
        x += 1
        z -= 1
    if nlist.count(x) > 0:
        print(x)
    else:
        print(z)
