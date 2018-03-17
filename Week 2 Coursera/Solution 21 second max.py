now = int(input())
nowMax = 1
secMax = 0

while now != 0:
    if now > nowMax and now != nowMax:
        secMax = nowMax
        nowMax = now
    else:
        if now > secMax:
            secMax = now
    now = int(input())
print(secMax)
