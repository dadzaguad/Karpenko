max = 0
nmax = 0
x = -1
while x != 0:
    x = int(input())
    if x > max:
        max, nmax = x, 1
    elif x == max:
        nmax += 1
print(nmax)
