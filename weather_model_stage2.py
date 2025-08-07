import math

print("Quadratic Equation: ax² + bx + c = 0")

try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("This is not a quadratic equation (a cannot be 0).")
    else:
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Two real and distinct roots: {root1} and {root2}")
        elif discriminant == 0:
            root = -b / (2 * a)
            print(f"One real root: {root}")
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-discriminant) / (2 * a)
            print(f"Complex roots: {real_part} ± {imaginary_part}i")

except ValueError:
    print("Invalid input. Please enter numerical values.")
