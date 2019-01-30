from collections import defaultdict
from itertools import combinations

from digit_tools import concatenate_digits, num_digits
from factor_tools import get_primes, is_prime

def is_prime_when_concatenated(first_prime, second_prime, prime_cache=None, prime_cache_max=None):
    """
    Is first_prime prepended to second_prime a prime, and vice versa?
    """
    a = concatenate_digits(first_prime, second_prime)
    if not is_prime(a, prime_cache, prime_cache_max):
        return False

    b = concatenate_digits(second_prime, first_prime)
    return is_prime(b, prime_cache, prime_cache_max)

def main():
    """
    Entry point
    """
    pair_set_size = 5
    
    # Grab a load of primes to work with
    max_digits_in_prime_cache = 4
    primes = get_primes(10 ** max_digits_in_prime_cache)
    prime_set = set(primes)

    # See which primes concatenate both ways to form new primes
    # We want the lowest sum of pair_set_size primes, so start with the smallest
    # and work our way up testing against all smaller primes
    prime_pairs = defaultdict(set)
    winning_sets = []
    for new_smallest_prime in primes:
        new_prime_pairs = set()
        for other_prime in prime_pairs.keys():
            if not is_prime_when_concatenated(new_smallest_prime, other_prime, prime_set, primes[-1]):
                continue

            # Yes, we have a valid pair
            new_prime_pairs.add(other_prime)
            prime_pairs[other_prime].add(new_smallest_prime)

            # Are the sets big enough?
            if len(new_prime_pairs) >= pair_set_size - 1:
                # Could be - check all pair combos that include our new pair
                possible_candidates = new_prime_pairs.union({new_smallest_prime})
                for candidate_set in combinations(possible_candidates, pair_set_size):
                    # See if all pairs work for this combo
                    is_winning_set = True
                    for pairwise_combo in combinations(candidate_set, 2):
                        if new_smallest_prime in set(pairwise_combo):
                            # We know this pair is fine already
                            continue
                        elif pairwise_combo[1] not in prime_pairs[pairwise_combo[0]]:
                            # This combination doesn't work
                            is_winning_set = False
                            break

                    if is_winning_set:
                        winning_sets.append(candidate_set)

            if winning_sets:
                break

        if winning_sets:
            break

        prime_pairs[new_smallest_prime] = new_prime_pairs

    # Get the best (smallest sum) winning set
    final_pair_set = min(winning_sets, key=lambda s: sum(s))
    print(f"Sum of {pair_set_size} primes: {sum(final_pair_set)} (primes: {final_pair_set})")

if __name__ == "__main__":
    main()
