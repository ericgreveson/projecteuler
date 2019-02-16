import math

def main():
    """
    Entry point
    """
    # We know d > 2n (as n/d < 1/2) and d < 3n (as n/d > 1/3) and n, d are coprime
    # We want d <= 12000. Check each denominator...
    count = 0
    for d in range(4, 12001):
        # For this denominator, we should check all coprime numerators greater than d/3 and smaller than d/2
        for n in range(d // 3, d // 2 + 1):
            if d < 3*n and d > 2*n and math.gcd(n, d) == 1:
                count += 1

    print(f"Count: {count}")

if __name__ == "__main__":
    main()
