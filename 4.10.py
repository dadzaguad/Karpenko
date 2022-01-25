from math import gcd


def reduce_fraction(n, m):
    k = gcd(n, m)
    p = n // k
    q = m // k
    return p, q


n = int(input())
m = int(input())
print(*reduce_fraction(n, m))
