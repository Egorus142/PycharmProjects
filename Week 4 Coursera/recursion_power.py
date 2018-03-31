a = a_init = float(input())
n = int(input())


def power(a, n):
    if n == 0:
        return(print(1))
    if n != 1:
        if n > 0:
            a *= a_init
            n -= 1
        power(a, n)
    else:
        print(a)


power(a, n)

