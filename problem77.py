from factor_tools import get_primes

def count_prime_ways(n, primes=None, cache=None):
    """
    Count the number of ways that n can be made from sum of at least 1 prime
    (or at least 2 primes if primes is initially None)
    primes: List of all primes we're allowed to use, from 2 upwards
    """
    # Get the prime lookup table once only
    if not primes:
        primes = get_primes(n)

    # Create memoizing cache with keys of (n, largest prime)
    if not cache:
        cache = {(2, 2): 1}

    cached_result = cache.get((n, primes[-1]), None)
    if cached_result:
        return cached_result

    # Special case if this is the last prime: can we get n from summing it i.e. is it a factor?
    if len(primes) == 1:
        # Well, we know the prime is 2. Is n even?
        ways = 1 if n % 2 == 0 else 0
        cache[(n, 2)] = ways
        return ways

    # Use the largest prime remaining
    largest_prime = primes[-1]
    remainder = n
    ways = 0

    while remainder > largest_prime:
        remainder -= largest_prime

        # No joy if remainder is 1 - can't make this from primes
        if remainder == 1:
            break

        # We can't use primes larger than remainder
        reverse_index = -2
        while primes[reverse_index] > remainder:
            reverse_index -= 1

        ways += count_prime_ways(remainder, primes[:reverse_index + 1], cache)

    if remainder == largest_prime:
        ways += 1

    # Now count all the ways with a smaller prime
    if len(primes) > 1:
        ways += count_prime_ways(n, primes[:-1], cache)

    cache[(n, largest_prime)] = ways
    return ways

def main():
    """
    Entry point
    """
    n = 10
    ways = 0
    while ways <= 5000:
        n += 1
        ways = count_prime_ways(n)

    print(f"n = {n} has {ways} ways")

if __name__ == "__main__":
    main()
