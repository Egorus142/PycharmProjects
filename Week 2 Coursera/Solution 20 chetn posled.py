now = int(input())
count = 0
while now != 0:
    if now % 2 == 0 and now != 1:
        count += 1
    now = int(input())
print(count)
