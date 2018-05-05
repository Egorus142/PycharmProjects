c = (list(range(int(input()))))
c1 = list(map(int, input().split()))
s = (list(range(int(input()))))
s1 = list(map(int, input().split()))
c1.sort()
s1.sort()

citizen = []
for i in range(len(c)):
    citizen.append((c[i], c1[i]))
    i += 1

shelters = []
for i in range(len(s)):
    shelters.append((s[i], s1[i]))
    i += 1


shelterlist = ...


for i in range(len(s)):
    if c1[i] - s1[i] > s1[i+1] - c1[i]:
        print(s[i])
    else:
        print(s[i + 1])
    i += 1

# shelter().sort(key=sorting2)
# print(citizen)
# print(shelters)



#def saver(x):

#
# print(s1.sort(key=saver))





#print(save)





'''def dist(point):
    return point[0] ** 2 + point[1] ** 2

n = int(input())
points = []
for i in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)
points.sort(key=dist)
for point in points:
    print(' '.join(map(str, point)))'''