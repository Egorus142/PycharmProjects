numbers = list(map(int, input().split()))
a = 0

for i in range(len(numbers)):
    if numbers[i] >= a:
        a = numbers[i]
        max = [a, i]

print(*max)
