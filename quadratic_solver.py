import sys
from math import isfinite


def read_coefficient(name: str) -> float:
    while True:
        try:
            value = float(input(f"{name}: "))
            if isfinite(value):
                return value
        except ValueError:
            pass
        print("Enter a finite number.", file=sys.stderr)


if __name__ == "__main__":
    a = read_coefficient("a")
    b = read_coefficient("b")
    c = read_coefficient("c")
