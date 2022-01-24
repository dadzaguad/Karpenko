s = input()
pos1 = s.find('h')
pos2 = s.rfind('h')
print(s[0:pos1], s[pos2 + 1:], sep='')
