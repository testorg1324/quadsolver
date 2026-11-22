from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from runpy import run_module
from unittest import TestCase
from unittest.mock import patch


class CoefficientInputTest(TestCase):
    def test_retries_invalid_values_and_reads_coefficients_in_order(self) -> None:
        stdin = StringIO("abc\n1e3\n\n-3\nNaN\n2.5\n")
        prompts, errors = StringIO(), StringIO()
        with patch("sys.stdin", stdin), redirect_stdout(prompts), redirect_stderr(errors):
            values = run_module("quadratic_solver", run_name="__main__")

        self.assertEqual([values[name] for name in "abc"], [1000.0, -3.0, 2.5])
        self.assertEqual(prompts.getvalue().split()[:6], ["a:", "a:", "b:", "b:", "c:", "c:"])
        self.assertEqual(len(errors.getvalue().splitlines()), 3)

    def test_solves_acceptance_examples(self) -> None:
        cases = (
            ("1\n-3\n2\n", "x1 = 2.0\nx2 = 1.0\n"),
            ("1\n2\n1\n", "x = -1.0\n"),
            ("1\n0\n1\n", "No real roots.\n"),
            ("0\n2\n-4\n", "x = 2.0\n"),
            ("0\n0\n5\n", "No real roots.\n"),
            ("0\n0\n0\n", "Infinitely many solutions.\n"),
        )
        for coefficients, expected in cases:
            with self.subTest(coefficients=coefficients):
                output = StringIO()
                with patch("sys.stdin", StringIO(coefficients)), redirect_stdout(output):
                    run_module("quadratic_solver", run_name="__main__")
                self.assertEqual(output.getvalue(), f"a: b: c: {expected}")
