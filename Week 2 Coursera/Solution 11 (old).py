a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

if (a1 * b1 * c1) == (a2 * b2 * c2):
    print('Boxes are equal')
else:
    if (a1 * b1 * c1) > (a2 * b2 * c2):
        print('The first box is larger than the second one')
    else:
        if (a1 * b1 * c1) < (a2 * b2 * c2):
            print('The first box is smaller than the second one')
        else:
            print('Boxes are incomparable')







