a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= d and b <= e or a <= e and b <= d:
    print('YES')
else:
    if c <= d and b <= e or c <= e and b <= d:
        print('YES')
    else:
        if a <= d and c <= e or a <= e and c <= d:
            print('YES')
        else:
            print('NO')
