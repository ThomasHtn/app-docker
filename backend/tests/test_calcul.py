import pytest
from modules.calcul import compute_square

def test_compute_square():
    assert compute_square(3) == 9
    assert compute_square(0) == 0
    assert compute_square(-4) == 16
