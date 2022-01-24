def isPointInSquare(x: float, y: float, v: float) -> bool:
    return (v ** 2 >= x ** 2) and (v ** 2 >= y ** 2)


x, y = float(input("x = ")), float(input("y = "))

print("YES" if isPointInSquare(x, y, 1) else "NO")
