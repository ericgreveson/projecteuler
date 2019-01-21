from factor_tools import compute_factors

def main():
    """
    Entry point
    """
    sum_factors = {i: sum(compute_factors(i)) for i in range(10000)}

    # Second pass: to check for amicability, we need to compute sum-factors for candidates over 10000
    extra_factors = dict()
    for i, sf_i in sum_factors.items():
        if sf_i >= 10000:
            extra_factors[sf_i] = sum(compute_factors(sf_i))

    sum_factors.update(extra_factors)

    # Compute set of amicable numbers below 10000

    amicable = {i for i, sf_i in sum_factors.items() if 1 < i < 10000 and i != sf_i and sum_factors[sf_i] == i}
    print(f"Sum-amicable-under-10k: {sum(amicable)}")
    return

if __name__ == "__main__":
    main()
