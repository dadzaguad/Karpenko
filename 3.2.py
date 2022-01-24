n = int(input())
i = 1
s = (sum([1 / (i ** 2) for i in range(1, n + 1)]))
print('{0:.6f}'.format(s))
