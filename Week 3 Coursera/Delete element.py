string = input()

size = len(string)

pos = string.find('h', 0)
reverse = string[::-1]
pos2 = reverse.find('h', 0)
posend = size - pos2

p1 = string[0:pos]
p2 = string[posend:size]

print(p1 + p2)
