string = str(input())
size = len(string)
x = string.find('f', 0)
y = string.find('f', size - x)

if x != y:
    print(y)
else:
    if x == y:
        print('-2')
    else:
        print('-1')
