now = int(input())
nowMax = 1
count = 0

while now != 0:
    if now == nowMax:
        count = count + 1
    else:
        if now > nowMax:
            nowMax = now
            count = 1
    now = int(input())
print(count)
