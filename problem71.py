from fractions import Fraction

def main():
    """
    Entry point
    """
    # Try all denominators up to 1000000, for the next value less than 3/7
    fracs = []
    for d in range(2, 1000001):
        # Numerator is the one that makes this fraction just less than 3/7
        # n / d < 3 / 7  =>  7n / 7d < 3d / 7d  =>  n < 3d / 7
        n = (3 * d) // 7 if (3 * d) % 7 != 0 else (3 * d) // 7 - 1
        fracs.append(Fraction(n, d))

    fracs = sorted(set(fracs))
    last_frac = fracs[-1]
    print(f"Fraction to the left of 3/7: {last_frac.numerator}/{last_frac.denominator}")

if __name__ == "__main__":
    main()
    