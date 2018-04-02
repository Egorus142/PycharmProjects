def recursion():
    n = int(input())
    if n == 0:
        print(n)
    else:
        recursion()
        print(n)


recursion()
