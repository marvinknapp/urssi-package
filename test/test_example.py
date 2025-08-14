import numpy as np
import pytest
from urssi_package.example import compute_statistics, better_hypot, hypot


@pytest.mark.parametrize(
    "a, b",
    [
        (3, 4),
        (5, 12),
        (8, 15),
        (0, 0),
        (1.5, 2.5),
        (-2, 5)
    ]
)
def test_hypot(a, b):
    expected = np.sqrt(a**2 + b**2)
    assert hypot(a, b) == expected


# test better hypot
@pytest.mark.parametrize(
    "a, b",
    [
        (3, 4),
        (5, 12),
        (8, 15),
        (0, 0),
        (42, -3),
        (1.5, 2.5),
        (-2, 5)
    ]
)
def test_better_hypot(a, b):
    expected = np.sqrt(a**2 + b**2)
    if a < 0 or b < 0:
        with pytest.raises(AssertionError):
            better_hypot(a, b)
    else:
        assert better_hypot(a, b) == expected