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


class TestBinomialProbability:
    @pytest.mark.parametrize("k, n, p, expected", [
        (3, 3, 0.5, 0.125),
        (1, 1, 0.5, 0.5),
        (1, 2, 0.5, 0.5),
    ])
    def test_known_values(self, k, n, p, expected):
        assert math_utils.binomial_probability(k, n, p) == pytest.approx(expected)

    @pytest.mark.parametrize("k, expected", [
        (0, 0.1681),
        (1, 0.3601),
        (2, 0.3087),
        (3, 0.1323),
        (4, 0.0283),
        (5, 0.0024),
    ])
    def test_matches_book(self, k, expected):
        actual = math_utils.binomial_probability(k, 5, 0.3)
        assert actual == pytest.approx(expected, abs=1e-4)

class TestBinomialDistribution:
    def test_fair_coin_two_flips(self):
        assert math_utils.binomial_distribution(2, 0.5) == pytest.approx([0.25, 0.5, 0.25])

    def test_has_one_entry_per_outcome(self):
        assert len(math_utils.binomial_distribution(10, 0.3)) == 11

    @pytest.mark.parametrize("n, p", [(1, 0.5), (10, 0.3), (50, 0.9)])
    def test_probabilities_sum_to_one(self, n, p):
        assert sum(math_utils.binomial_distribution(n, p)) == pytest.approx(1)
