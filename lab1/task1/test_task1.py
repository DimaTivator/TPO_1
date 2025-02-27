import pytest
import numpy as np
from task1 import arccos_series


def test_basic_values():
    test_cases = [
        (0, np.pi / 2),
        (0.5, np.pi / 3),
        (-0.5, 2 * np.pi / 3),
    ]
    for x, expected in test_cases:
        assert pytest.approx(arccos_series(x, 100), rel=1e-5) == expected


def test_extreme_values():
    for x in np.linspace(0.8, 0.95, 10):
        assert pytest.approx(arccos_series(x, 20), rel=1e-2) == np.arccos(x)
    assert pytest.approx(arccos_series(1, 50), rel=1) == 0
    assert pytest.approx(arccos_series(-1, 50), rel=1) == np.pi


def test_symmetry():
    for x in np.linspace(-1, 1, 10):
        assert pytest.approx(arccos_series(-x, 20), rel=1e-5) == np.pi - arccos_series(
            x, 20
        )


def test_accuracy_compared_to_numpy():
    for x in np.linspace(-0.8, 0.8, 10):
        assert pytest.approx(arccos_series(x, 20), rel=1e-5) == np.arccos(x)


def test_accuracy_by_n_terms():
    for x in np.linspace(-1, 1, 10):
        ground_truth = np.arccos(x)
        for n_terms in range(1, 20):
            assert abs(arccos_series(x, n_terms + 1) - ground_truth) <= abs(
                arccos_series(x, n_terms) - ground_truth
            )


def test_out_of_domain():
    for x in [-1.1, 1.1, 2, -2]:
        with pytest.raises(ValueError):
            arccos_series(x, 10)
