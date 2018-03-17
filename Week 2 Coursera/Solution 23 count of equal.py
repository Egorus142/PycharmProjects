p = -1
curr = 0
m = 0
element = int(input())
while element != 0:
    if p == element:
        curr += 1
    else:
        p = element
        m = max(m, curr)
        curr = 1
    element = int(input())
m = max(m, curr)
print(m)
