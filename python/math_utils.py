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

def binomial_distribution(count_of_events, number_of_trials, event_probability):
    k = count_of_events
    n = number_of_trials
    p = event_probability
    return m_choose_k(n, k)*(p**k)*(1-p)**(n-k)
