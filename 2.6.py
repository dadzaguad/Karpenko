a, b, c = int(input()), int(input()), int(input())
if a <= b <= c:
    print(a, b, c)
else:
    if b <= a <= c:
        print(b, a, c)
    else:
        if a <= c <= b:
            print(a, c, b)
        else:
            if b <= c <= a:
                print(b, c, a)
            else:
                if c <= b <= a:
                    print(c, b, a)
                else:
                    print(c, a, b)
