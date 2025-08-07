import math

def solve_quadratic(a, b, c, index):
    print(f"\nEquation {index + 1}: a={a}, b={b}, c={c}")
    if a == 0:
        print("Not a quadratic equation (a = 0)")
        return

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

try:
    with open("inputs.txt", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip() == "":
            continue  # skip empty lines
        try:
            a, b, c = map(float, line.strip().split())
            solve_quadratic(a, b, c, i)
        except ValueError:
            print(f"\nEquation {i + 1}: Invalid input format: {line.strip()}")

except FileNotFoundError:
    print("Error: inputs.txt file not found.")

