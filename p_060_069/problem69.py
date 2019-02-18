from factor_tools import next_prime, totient

def main():
    """
    Entry point
    """
    # This is a very slow and thick approach. See problem70 for a nicer way.
    best = (2, 2)
    primes = [2]
    for i in range(3, 1000001):
        # Get all primes up to i
        while primes[-1] < i:
            primes.append(next_prime(primes[-1]))

        phi = totient(i, primes)
        quotient = i / phi
        if quotient > best[1]:
            best = (i, quotient)

    print(f"Best: n={best[0]} with n/phi={best[1]}")

if __name__ == "__main__":
    main()
