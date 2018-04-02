def sum(b):
    a = int(input())
    if a != 0:
        b += a
        sum(b)
    else:
        print(b)


b = 0
sum(b)
