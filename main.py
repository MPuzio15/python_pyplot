from math import sqrt

# quadratic equation

while True:
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        break
    except ValueError:
        print("Niepoprawna wartosc")
    # end try
# end while

# delta
d = b * b - 4 * a * c

if d >= 0:
    # sqrt from delta
    p = sqrt(d)
    x1 = (-b - p) / (2 * a)
    x2 = (-b + p) / (2 * a)
    print(f"x1={x1:0.1f} x2={x2:0.1f}")
else:
    print("No results")

