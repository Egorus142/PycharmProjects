a = int(input())
b = int(input())
c = int(input())

if a >= b >= c:
    (a, b, c) = (c, b, a)
else:
    if a >= c >= b:
        (a, b, c) = (b, c, a)
    else:
        if c >= b >= a:
            (a, b, c) = (a, b, c)
        else:
            if c >= a >= b:
                (a, b, c) = (b, a, c)
            else:
                if b >= a >= c:
                    (a, b, c) = (c, a, b)
                else:
                    (a, b, c) = (a, c, b)

print(a, b, c)

# abc, acb, cba, cab, bac, bca

# abc
# acb
# cba
# cab
# bac
# bca
