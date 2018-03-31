a = float(input())
b = int(input())


def sum(a, b):
    if b != 0:
            a += 1
            b -= 1
            sum(a, b)
    else:
        print(int(a))


sum(a, b)
