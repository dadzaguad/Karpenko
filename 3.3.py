from math import *

X = float(input())
if X > 1:
    n = X - floor(X)
    print(round(n, 4))
else:
    print(X)
