from fractions import Fraction

from digit_tools import is_permutation
from factor_tools import get_primes, totient

def main():
    """
    Entry point
    """
    # (After reading the pdf for problem 69...!) we know n/phi(n) = prod(p / (p-1))
    # for p in all the primes dividing n.
    # Therefore n/phi(n) is at a minimum when prod(p / (p-1)) is at a minimum
    # which would happen when we have a small number of large prime factors.
    # Because phi(prime) = prime - 1, we can't use just one prime as phi(p) won't be a permutation of p
    # We should check composites of a couple of primes. Up to 10^5 should do
    # because we want two primes as high as possible
    print("Getting primes below 100000...")
    primes = get_primes(100000)
    
    # Now search combinations of two primes 
    print("Searching products of two primes for phi(p) == permutation(p)...")
    best = None
    for index, p1 in enumerate(primes):
        for p2 in primes[index+1:]:
            n = p1 * p2
            if n > 10 ** 7:
                break

            phi = n * (1 - Fraction(1, p1)) * (1 - Fraction(1, p2))
            if is_permutation(n, phi):
                print(f"Hello: {n} = {p1} * {p2}")
                if not best or (best[2] >= n/phi):
                    best = (n, phi, n/phi)

    print(f"Best: n={best[0]}, with phi(n)={best[1]}")

if __name__ == "__main__":
    main()
