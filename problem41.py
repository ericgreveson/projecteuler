import itertools

from factor_tools import is_prime

def main():
    """
    Entry point
    """
    candidates = []
    for num_digits in range(4, 10):
        for perm in itertools.permutations(range(1, num_digits + 1), num_digits):
            n = 0
            for index, digit in enumerate(perm):
                n += digit * (10 ** index)

            if is_prime(n):
                candidates.append(n)
                print(n)

    print(f"Highest: {max(candidates)}")

if __name__ == "__main__":
    main()
