from collections import defaultdict

from digit_tools import concatenate_digits, num_digits
from factor_tools import get_primes, is_prime

def main():
    """
    Entry point
    """
    pair_set_size = 4
    
    # Grab a load of primes to work with
    max_digits_in_prime_cache = 4
    primes = get_primes(10 ** max_digits_in_prime_cache)
    prime_set = set(primes)

    # See which primes concatenate both ways to form new primes
    prime_pairs = defaultdict(set)
    big_enough = []
    for first_index, first_prime in enumerate(primes):
        final_pair_set = None
        for second_prime in primes[first_index+1:]:
            a = concatenate_digits(first_prime, second_prime)
            if not is_prime(a, prime_set, primes[-1]):
                continue

            b = concatenate_digits(second_prime, first_prime)
            if not is_prime(b, prime_set, primes[-1]):
                continue

            # Yes, we have a valid pair
            prime_pairs[first_prime].add(second_prime)
            prime_pairs[second_prime].add(first_prime)

            # Are the sets big enough?
            for key in [first_prime, second_prime]:
                if len(prime_pairs[key]) == pair_set_size - 1:
                    # Put this in our "known big enough" collection and add the key for simplicity
                    prime_pairs[key].add(key)
                    big_enough.append(prime_pairs[key])
                    print(f"Found possible set: {prime_pairs[key]}")

            if len(big_enough) >= pair_set_size:
                # We might have a solution. Check the all-pairs intersection
                possible_solution = big_enough[0]
                for pair_set in big_enough[1:]:
                    possible_solution = possible_solution.intersection(pair_set)

                if len(possible_solution) >= pair_set_size:
                    final_pair_set = sorted(possible_solution)
                    print(f"Found our set: {final_pair_set}")
                    break
        
        if final_pair_set:
            break

    print(f"Sum of {pair_set_size} primes: {sum(final_pair_set)}")

if __name__ == "__main__":
    main()
