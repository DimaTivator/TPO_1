import pytest
import numpy as np
from task1 import arccos_series


@pytest.mark.parametrize("x, expected", [
    (0, np.pi / 2),
    (0.5, np.pi / 3),
    (-0.5, 2 * np.pi / 3),
])
def test_basic_values(x, expected):
    assert pytest.approx(arccos_series(x, 100), rel=1e-5) == expected


@pytest.mark.parametrize("x, n, rel, expected", [
    (0.8, 20, 1e-2, np.arccos(0.8)),
    (0.9, 20, 1e-2, np.arccos(0.9)),
    (1, 100, 1, 0),
    (-0.8, 20, 1e-2, np.arccos(-0.8)),
    (-0.9, 20, 1e-2, np.arccos(-0.9)),
    (-1, 100, 1, np.pi),
])
def test_extreme_values(x, n, rel, expected):
    assert pytest.approx(arccos_series(x, n), rel=rel) == expected


@pytest.mark.parametrize("x", [-1.1, 1.1, 2, -2])
def test_out_of_domain(x):
    with pytest.raises(ValueError):
        arccos_series(x, 10)


@pytest.mark.parametrize("x", np.linspace(-1, 1, 10))
def test_symmetry(x):
    assert pytest.approx(arccos_series(-x, 20), rel=1e-5) == np.pi - arccos_series(x, 20)


def test_accuracy_by_n_terms():
    for x in np.linspace(-1, 1, 10):
        ground_truth = np.arccos(x)
        for n_terms in range(1, 20):
            assert abs(arccos_series(x, n_terms + 1) - ground_truth) <= abs(
                arccos_series(x, n_terms) - ground_truth
            )
