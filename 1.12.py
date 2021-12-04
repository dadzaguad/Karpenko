A = int(input())
B = int(input())
N = int(input())
rub = (B * N) // 100 + A * N
cop = B * N % 100
print(rub, cop)
