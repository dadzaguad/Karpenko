n = int(input())
start = 10 ** n - 1
end = 10 ** (n - 1) - 1
print(*range(start, end, -2))
