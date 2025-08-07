import math

try:
    with open("input.txt", "r") as file:
        line = file.readline()
        a, b, c = map(float, line.strip().split())

    print(f"Read from file: a={a}, b={b}, c={c}")

    if a == 0:
        print("Not a quadratic equation (a cannot be 0).")
    else:
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Two real and distinct roots: {root1}, {root2}")
        elif discriminant == 0:
            root = -b / (2 * a)
            print(f"One real root: {root}")
        else:
            real = -b / (2 * a)
            imag = math.sqrt(-discriminant) / (2 * a)
            print(f"Complex roots: {real} ± {imag}i")

except FileNotFoundError:
    print("input.txt not found.")
except ValueError:
    print("Check the input format. It should be: a b c")

