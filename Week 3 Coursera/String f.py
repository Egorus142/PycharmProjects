string = input()
pos = string.find('f', 0)
pos2 = string.find('f', -1)

if pos != pos2:
    print(pos, pos2)
else:
    if pos == pos2 and pos != -1:
        print(pos)
