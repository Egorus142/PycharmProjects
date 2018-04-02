a = str(input())

s1 = a.find('h')
s2 = a.rfind('h') - 1
s = a[s1:s2]

print(a[0:s1 + 1] + s.replace('h', 'H') + a[-1:s2:-1])
