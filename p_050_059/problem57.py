from fractions import Fraction

from digit_tools import num_digits

def main():
    """
    Entry point
    """
    denom = 2
    heavy_num_count = 0
    for i in range(1000):
        root_2_approx = 1 + Fraction(1, denom)
        denom = 2 + Fraction(1, denom)
        if num_digits(root_2_approx.numerator) > num_digits(root_2_approx.denominator):
            heavy_num_count += 1

    print(f"Number of top-heavy approximations: {heavy_num_count}")

if __name__ == "__main__":
    main()
    