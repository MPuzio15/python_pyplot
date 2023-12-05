from math import sqrt

# quadratic equation

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# delta
d = b * b - 4 * a * c

if d >= 0:
    # sqrt from delta
    p = sqrt(d)
    x1 = (-b - p) / (2 * a)
    x2 = (-b + p) / (2 * a)
    print("x1 = ", x1)
    print('x2 = ', x2)
else:
    print("No results")

