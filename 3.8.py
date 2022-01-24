a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
D = a * d - b * c
Dx = e * d - b * f
Dy = a * f - e * c
x = Dx / D
y = Dy / D
print(x, y)
