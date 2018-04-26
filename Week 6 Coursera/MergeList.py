a = list(map(int, input().split()))
b = list(map(int, input().split()))


def merge(a, b):
    a.extend(b)
    c = a
    c.sort()
    print(*c)


merge(a, b)
