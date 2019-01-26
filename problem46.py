import math

from factor_tools import is_prime

def next_prime(previous):
    """
    Get the next prime after previous
    """
    i = previous + 1
    while True:
        if is_prime(i):
            return i

        i += 1

def main():
    """
    Entry point
    """
    i = 33
    primes = [2]
    while True:
        # We're only interested in odd composite numbers
        if is_prime(i):
            i += 2
            continue

        # Can we compose this from a prime and twice a square?
        # Make sure we have enough primes
        while primes[-1] < i:
            primes.append(next_prime(primes[-1]))

        # Check primes, but not 2 as it's even and then the rest won't work out
        found_one = False
        for p in primes[1:-1]:
            # Is the remainder twice a square?
            half_remainder = (i - p) // 2
            root = math.sqrt(half_remainder)
            if int(root) ** 2 == half_remainder:
                # This one works...
                found_one = True
                break

        if not found_one:
            break

        i += 2

    print(f"This doesn't work: {i}")

if __name__ == "__main__":
    main()
