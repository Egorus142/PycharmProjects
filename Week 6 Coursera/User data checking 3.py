A, B = map(int, input().split())
volume = sorted([int(input()) for _ in range(B)])
amount = sum(volume)

while amount > A and B:
    amount -= volume.pop()
    B -= 1

print(B)
