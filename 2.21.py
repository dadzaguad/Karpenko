a = int(input())
b = 1
c = 1
while a != 0:
    d = int(input())
    if d == a:
        b += 1
    else:
        if b > c:
            c = b
        a = d
        b = 1
print(c)
