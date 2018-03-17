string = input()
a = string.find('f', 0)
b = string.rfind('f', 0)

if a == b and a == -1:
    print('')
else:
    if a == b:
        print(a)
    else:
        print(a, b)
