import itertools

from digit_tools import num_digits
from factor_tools import get_primes

def main():
    """
    Entry point
    """
    # Get a bunch of primes to test. Guess how many digits we might need to search up to.
    max_num_digits = 6
    family_size = 8
    primes = get_primes(10 ** max_num_digits)

    # We know the first prime with 8 family members will be > 56003, try 5 digits first
    for n_digits in range(5, max_num_digits + 1):
        print(f"Trying {n_digits} digits...")

        # Get the set of candidates for this digit count
        n_digit_primes = [p for p in primes if num_digits(p) == n_digits]
        n_digit_prime_set = set(n_digit_primes)

        for base_prime in n_digit_primes:
            # We want at least 8 primes, so we need to have the last digit as 1, 3, 5, or 7
            # (i.e. the last digit of this prime can't be a replacement candidate)
            for num_replacement_digits in range(1, n_digits):
                digit_pattern = [1] * num_replacement_digits + [0] * (n_digits - 1 - num_replacement_digits)
                for replacement_pattern in set(itertools.permutations(digit_pattern, n_digits - 1)):
                    # We need family_size primes, so as soon as we have (10 - family_size + 1) non-primes, we're "bust"
                    num_non_primes = 0
                    for replacement_digit in range(10):
                        # Make the replacement (counting digits from right to left)
                        candidate = 0
                        for digit in range(n_digits):
                            digit_multiplier = 10 ** digit
                            if digit == 0 or not replacement_pattern[-digit]:
                                # Use the original digit
                                candidate += ((base_prime // digit_multiplier) % 10) * digit_multiplier
                            else:
                                # Use the replacement digit
                                candidate += replacement_digit * digit_multiplier

                        # Test it
                        if candidate not in n_digit_prime_set:
                            num_non_primes += 1
                            if num_non_primes > 10 - family_size:
                                # Next replacement pattern
                                break

                    if num_non_primes <= (10 - family_size):
                        # We found it!
                        print(f"Found prime: {base_prime}, replacement pattern: {replacement_pattern}")
                        return

    print("Found nothing :-(")

if __name__ == "__main__":
    main()
