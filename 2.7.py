a, b, c = int(input()), int(input()), int(input())
if a == b != c or b == c != a or c == a != b:
    print(2)
else:
    if b == c == a:
        print(3)
    else:
        print(0)
