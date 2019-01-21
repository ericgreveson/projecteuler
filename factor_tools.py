def compute_factors(n):
    """
    Return a list of all factors (proper divisors) of a number n, including 1
    """
    return [i for i in range(1, n // 2 + 1) if n % i == 0]
