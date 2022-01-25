def power(a, n):
    aⁿ = a * a**(n - 1)
    return aⁿ


a = float(input())
n = int(input())
print(power(a, n))
