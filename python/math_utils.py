import math


def m_choose_k(m, k) -> int:
    """
    Calculate the binomial coefficient (m choose k).

    In theory we could do math.comb(m, k)

    Args:
        m (int): The total number of items.
        k (int): The number of items to choose.

    Returns:
        int: The number of combinations of choosing k items from m items.
    """
    return math.factorial(m) // (math.factorial(k) * math.factorial(m - k))
