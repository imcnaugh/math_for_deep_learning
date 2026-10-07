import unittest

from python import math_utils


class MyTestCase(unittest.TestCase):

    def simple_m_choose_k_test(self):
        self.assertEqual(math_utils.m_choose_k(2, 2), 1)

    def test_m_choose_k(self):
        self.assertEqual(math_utils.m_choose_k(10, 2), 45)


if __name__ == '__main__':
    unittest.main()
