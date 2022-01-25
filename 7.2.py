n, b = list(map(int, input().split())), list(map(int, input().split()))
print(*sorted(set(n) & set(b)))
