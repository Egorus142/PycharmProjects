a = int(input())
b = int(input())
c = int(input())

if a == b and a == c:
    print(3)
else:
    if a == b or a == c or b == c:
        print(2)
    else:
        print(0)
