s = input()
pos = s.find('f')
num = 0
if pos != -1:
    num += 1
    while pos < len(s) - 1:
        pos += 1
        if s[pos] == "f":
            num += 1
            if num == 2:
                print(pos)

if num == 1:
    print('-1')
if s.find('f') == -1:
    print('-2')
