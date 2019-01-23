from factor_tools import compute_factors

def main():
    """
    Entry point
    """
    # Compute set of all abundant numbers up to the limit we know all integers above can be
    # expressed as a sum of two abundant numbers
    sum_abundant_limit = 28123
    abundant = {i for i in range(1, sum_abundant_limit) if sum(compute_factors(i)) > i}
    print(f"Found {len(abundant)} abundant numbers")

    # Now compute set of numbers which are a sum of two of the above
    sum_two_abundant = {i + j for i in abundant for j in abundant}
    print(f"Found {len(sum_two_abundant)} sum-two-abundant")

    # And compute the sum of all non-sum-two abundant numbers
    sum_non_sum_two_abundant = sum(i for i in range(1, sum_abundant_limit) if i not in sum_two_abundant)
    print(f"Total sum of non-sum-two-abundant numbers: {sum_non_sum_two_abundant}")

if __name__ == "__main__":
    main()
