n = int(input())
data = []

for i in range(n):
    x = str(input())
    list1 = x.split(' ')
    data.append(list1)

data.sort(key=lambda i: (i[0]))
data.sort(key=lambda i: (i[1]), reverse=True)

for i in range(n):
    print(data[i][0])
