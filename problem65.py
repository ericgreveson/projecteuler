from fractions import Fraction

from digit_tools import get_digits

def main():
    """
    Entry point
    """
    # Get first 100 sequence elements of e
    seq = [2]
    for i in range(1, 34):
        seq += [1, 2*i, 1]

    # Now compute this as a convergent. Easiest way is back to front
    f = Fraction(0)
    for s in reversed(seq):
        f = Fraction(1, s + f)

    # Lastly, we need to invert
    f = Fraction(1, f)

    sum_digits_num = sum(get_digits(f.numerator))
    print(f"Sum digits of convergent_e(100): {sum_digits_num}")

if __name__ == "__main__":
    main()
