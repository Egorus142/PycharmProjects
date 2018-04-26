numbers = list(map(int, input().split()))
a = 1000

for i in range(len(numbers)):
    if numbers[i] < a and numbers[i] > 0:
        a = numbers[i]
        min = [a]

print(*min)
