a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d == b + 1 or d == b - 1 or d == b:
    if c == a + 1 or c == a - 1 or c == a:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
