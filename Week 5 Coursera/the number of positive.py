numbers = list(map(int, input().split()))
a = 0
for i in range(len(numbers)):
    if numbers[i] == 0:
        a = a
    elif numbers[i] >= 0:
        a += 1

print(a)
