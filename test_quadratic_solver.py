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
        self.assertEqual(prompts.getvalue().split(), ["a:", "a:", "b:", "b:", "c:", "c:"])
        self.assertEqual(len(errors.getvalue().splitlines()), 3)
