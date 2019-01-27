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

def next_prime(previous):
    """
    Get the next prime after previous
    """
    i = previous + 1
    while True:
        if is_prime(i):
            return i

        i += 1
        
def compute_prime_factors(n):
    """
    Compute all prime factors of a number n
    Some prime factors may be repeated e.g. 12 has prime factors [2, 2, 3]
    """
    prime_factors = []
    current_prime = 2
    remainder = n
    while remainder > 1:
        # Divide by the current prime as many times as we can
        while remainder % current_prime == 0:
            prime_factors.append(current_prime)
            remainder //= current_prime

        # Find next prime
        current_prime = next_prime(current_prime)

    return prime_factors

def get_primes(up_to):
    """
    Get all primes up to (but not including) up_to
    """
    primes = [2]
    while primes[-1] < up_to:
        primes.append(next_prime(primes[-1]))

    return primes[:-1]
    