def power(a, n):
    if 0 == a:
        return 0
    if 0 == n:
        return 1
    if n % 2 == 0:
        return power(a, n / 2) ** 2
    return a * power(a, n - 1)


a = float(input())
n = int(input())
print(power(a, n))
