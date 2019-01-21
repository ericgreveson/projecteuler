def compute_factors(n):
    """
    Return a list of all factors (proper divisors) of a number n, including the factor 1
    """
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def is_prime(n):
    """
    Return true if n is prime (n>1)
    """
    # Slight optimization to quickly reject even numbers
    return n == 2 or (n % 2 == 1 and len(compute_factors(n)) == 1)
