import sys
from math import isfinite, sqrt


def read_coefficient(name: str) -> float:
    while True:
        try:
            value = float(input(f"{name}: "))
            if isfinite(value):
                return value
        except ValueError:
            pass
        print("Enter a finite number.", file=sys.stderr)


def print_solution(a: float, b: float, c: float) -> None:
    if a == 0:
        if b != 0:
            print(f"x = {-c / b}")
        elif c != 0:
            print("No real roots.")
        else:
            print("Infinitely many solutions.")
        return

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("No real roots.")
        return

    root = sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    if discriminant == 0:
        print(f"x = {x1}")
        return

    x2 = (-b - root) / 2 * a
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")


if __name__ == "__main__":
    a = read_coefficient("a")
    b = read_coefficient("b")
    c = read_coefficient("c")
    print_solution(a, b, c)
