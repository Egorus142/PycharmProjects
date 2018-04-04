a = int(input())
b = int(input())-1

if a < b:
    for i in range(a, b + 2):
        print(i)
else:
    for i in range(a, b, -1):
        print(i)
