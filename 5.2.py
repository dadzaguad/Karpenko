A = int(input())
B = int(input())
if A > B:
    for i in range(A, B - 1, -1):
        print(i, end=' ')
else:
    for j in range(A, B + 1):
        print(j, end=' ')
