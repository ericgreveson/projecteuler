def nth_triangle(n):
    """
    Compute the nth triangle number
    """
    return n * (n + 1) // 2

def nth_pentagonal(n):
    """
    Compute the nth pentagonal number
    """
    return n * (3 * n - 1) // 2

def nth_hexagonal(n):
    """
    Compute the nth hexagonal number
    """
    return n * (2 * n - 1)

def main():
    """
    Entry point
    """
    n = 286
    pentagonal = set([nth_pentagonal(i) for i in range(n)])
    hexagonal = set([nth_hexagonal(i) for i in range(n)])
    while True:
        # Keep the lists updated to make sure we have enough to check
        pentagonal.add(nth_pentagonal(n))
        hexagonal.add(nth_hexagonal(n))
        triangle = nth_triangle(n)
        if triangle in pentagonal and triangle in hexagonal:
            break

        n += 1

    print(f"Next triangle number with pent and hex: {triangle}")

if __name__ == "__main__":
    main()
