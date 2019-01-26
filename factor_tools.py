import math

def compute_factors(n):
    """
    Return a list of all factors (proper divisors) of a number n, including the factor 1
    """
    factors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return factors

def is_prime(n):
    """
    Return true if n is prime (n>1)
    """
    # Optimizations to quickly reject known non-primes
    if n in [2, 3, 5, 7]:
        return True

    if (n % 10) not in [1, 3, 7, 9] or n == 1:
        return False

    return len(compute_factors(n)) == 1
