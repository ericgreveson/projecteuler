from factor_tools import get_primes, totient

def main():
    """
    Entry point
    """
    # We have n/d where n<d. For reduced proper fractions, n and d must be coprime.
    # So for denominator d, there are phi(d) numerators, and we want sum(phi(d)), 1 < d <= 10^6
    print("Getting primes up to 1000000...")
    primes = get_primes(1000000)

    print("Summing phi(n)...")
    phi_sum = 0
    for n in range(2, 1000001):
        if n % 10000 == 0:
            print(f"{n}")
        phi_sum += totient(n, primes)

    print(f"sum(phi(n)): {phi_sum}")

if __name__ == "__main__":
    main()
