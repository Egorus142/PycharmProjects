mfile = open("input.txt", "r", encoding="utf8")
xyz = int(mfile.readline())
myList = []

for line in mfile:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        myList.append(newLine)
mfile.close()
myList.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
myList.reverse()

konk = []
for i in myList:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    konk.append(sum)
n = len(konk)


def konkurs(n, xyz, konk):
    if n <= xyz:
        return 0
    elif konk[xyz] == konk[0]:
        return 1
    for i in range(xyz, 0, -1):
        if konk[i] < konk[i - 1]:
            return konk[i - 1]


print(konkurs(n, xyz, konk))
