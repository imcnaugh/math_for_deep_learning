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

def binomial_probability(count_of_events: int, number_of_trials: int, event_probability: float) -> float:
    k = count_of_events
    n = number_of_trials
    p = event_probability
    return m_choose_k(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binomial_distribution(number_of_trials, event_probability):
    return [
        binomial_probability(k, number_of_trials, event_probability)
        for k in range(number_of_trials + 1)
    ]