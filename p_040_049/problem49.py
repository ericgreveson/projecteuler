from digit_tools import get_digits
from factor_tools import get_primes

def main():
    """
    Entry point
    """
    # Get all primes up to 10000
    primes = get_primes(10000)

    prime_set = set(primes)

    triples = []
    for first_prime_index, first_prime in enumerate(primes):
        if first_prime < 1000:
            continue

        # OK, let's see if this and any other prime will form an arithmetic seq to get a third
        for second_prime_index in range(first_prime_index + 1, len(primes)):
            second_prime = primes[second_prime_index]
            third_prime_candidate = 2 * second_prime - first_prime
            if third_prime_candidate in prime_set:
                # Are the numbers permutations of one another?
                p1_digits = get_digits(first_prime)
                p2_digits = get_digits(second_prime)
                p3_digits = get_digits(third_prime_candidate)
                if sorted(p1_digits) == sorted(p2_digits) == sorted(p3_digits):
                    triples.append((first_prime, second_prime, third_prime_candidate))
                    print(f"Triple found! {triples[-1]}")

if __name__ == "__main__":
    main()
