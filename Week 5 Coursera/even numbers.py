numbers = list(map(int, input().split()))
newlist = []
for i in range(len(numbers)):
    if numbers[i] >= 0:
        newlist.append(numbers[i])

print(*newlist)
