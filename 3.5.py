from math import *
n = float(input())
z = n - floor(n)
if z < 0.5:
    x = floor(n)
else:
    x = ceil(n)
print(x)
