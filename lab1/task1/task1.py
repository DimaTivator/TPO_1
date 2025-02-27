import numpy as np
from math import factorial


def arccos_series(x: float, n_terms: int = 10):
    if abs(x) > 1:
        raise ValueError("x must be in [-1, 1]")

    result = np.pi / 2
    for n in range(n_terms):
        coeff = factorial(2 * n) / (4**n * (factorial(n) ** 2) * (2 * n + 1))
        result -= coeff * x ** (2 * n + 1)
    return result
