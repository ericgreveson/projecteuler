from math import gcd

def get_primitive_pythagorean_triples(max_length):
    """
    Get Pythagorean triples up to a+b+c <= max_length
    """
    # Use Euclid's formula: choose coprime numbers m, n with m > n > 0, m, n not both odd
    # Then a = m^2 - n^2, b = 2*m*n, c = m^2 + n^2
    triples = []
    n = 1
    while True:
        n_squared = n * n

        # n + 1 will always be coprime to n
        m = n + 1

        while True:
            m_squared = m * m
            a = m_squared - n_squared
            b = 2 * m * n
            c = m_squared + n_squared

            # Have we exceeded max_length?
            if a + b + c > max_length:
                break

            # We have a triple!
            a, b = min(a, b), max(a, b)
            if a % 2 != 0 or b % 2 != 0:
                triples.append((a, b, c))

            # Find next m coprime to n
            # Only use even m if n is odd (m and n both odd is not a primitive triple)
            # and vice versa, since we know m and n both even means gcd(m, n) is at least 2
            m += 1
            while (n % 2 == m % 2) or gcd(m, n) > 1:
                m += 1

        # Did we bail out of the inner loop without incrementing m?
        if m == n + 1:
            return triples

        n += 1

def main():
    """
    Entry point
    """
    # First, get all primitive Pythagorean triples with total length less than 1500000
    max_len = 1500000
    print("Finding primitive triples...")
    primitive_triples = get_primitive_pythagorean_triples(max_len)

    # Now work out how many L values have exactly one
    length_counts = [0] * (max_len + 1)
    for t in primitive_triples:
        l = t[0] + t[1] + t[2]
        for multiplier in range(1, max_len // l + 1):
            length_counts[l * multiplier] += 1

    singular_count = sum([1 for count in length_counts if count == 1])
    print(f"{singular_count} lengths can form a single triangle")

if __name__ == "__main__":
    main()
