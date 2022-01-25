n = list(map(int, input().split()))
x = set()
for num in n:
    if num in x:
        print('YES')
    else:
        print('NO')
        x.add(num)
        