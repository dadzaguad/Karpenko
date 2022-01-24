s = input()
pos1 = s.find('f')
pos2 = s.rfind('f')
if pos1 == -1:
    print()
elif pos1 == pos2:
    print(pos1)
else:
    print(pos1, pos2)
