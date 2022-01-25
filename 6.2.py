b = int(input())
a = list(map(int, input().split()))
if b == len(a):
    a.sort()
    print(*a)
