n = int(input())
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
print((a - d)**2 + (c - b)**2 + 1)
