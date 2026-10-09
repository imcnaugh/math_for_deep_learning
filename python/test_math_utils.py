import math

import pytest

import math_utils

class TestMChooseK:
    @pytest.mark.parametrize("m, k, expected", [
        (2, 2, 1),
        (10, 2, 45),
        (5, 0, 1),
    ])
    def test_known_values(self, m, k, expected):
        assert math_utils.m_choose_k(m, k) == expected

    def test_matches_stdlib(self):
        assert math_utils.m_choose_k(20, 7) == math.comb(20, 7)


class TestBinomialDistribution:
    @pytest.mark.parametrize("k, n, p, expected", [
        (3, 3, 0.5, 0.125),
        (1, 1, 0.5, 0.5),
        (1, 2, 0.5, 0.5),
        (2, 4, 0.5, 0.375),
    ])
    def test_known_values(self, k, n, p, expected):
        assert math_utils.binomial_distribution(k, n, p) == pytest.approx(expected)
