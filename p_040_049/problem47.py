from factor_tools import prime_factors

def main():
    """
    Entry point
    """
    num_prime_factors = {}
    i = 1
    while True:
        all_have_four = True
        for j in range(4):
            n = i + j
            if n in num_prime_factors:
                npf = num_prime_factors[n]
            else:
                # This is a bit slow, should really keep the already computed primes around
                npf = len(set(prime_factors(n)))
                num_prime_factors[n] = npf

            if npf != 4:
                all_have_four = False
            
        if all_have_four:
            break

        i += 1

    print(f"First with 4 prime factors consecutively: {i}")

if __name__ == "__main__":
    main()
