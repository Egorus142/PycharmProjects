c = int(input())
fst = c // 10
sec = c - fst * 10
y = ()
if c > 9 and c < 21:
    y = 'korov'
else:
    if c == 1 or sec == 1:
        y = 'korova'
    else:
        if c == 2 or c == 3 or c == 4 or sec == 2 or sec == 3\
                or sec == 4:
            y = 'korovy'
        else:
            y = 'korov'

print(c, y)
