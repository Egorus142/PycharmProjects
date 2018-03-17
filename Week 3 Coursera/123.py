s = input()
k = 0
for i in range(len(s)):
    if s[i] == 'f':
        k += 1
        if k == 2:
            print(i)
if (s.count('f')) == 1:
    print(-1)
if (s.count('f')) == 0:
    print(-2)
