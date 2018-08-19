a = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
students = []

for list in a:
    b = list.rstrip('\n')
    x = b.split(' ')
    list2 = [x[0], x[1], x[3]]
    students.append(list2)


students.sort()

for item in students:
    print(' '.join(item), sep='\n', file=outFile)


a.close()
outFile.close()
