from fractions import Fraction
from functools import reduce

def main():
    """
    Entry point
    """
    # We consider fractions with two digits in num and denom, less than one
    curious = []
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            nums = numerator // 10, numerator % 10
            denoms = denominator // 10, denominator % 10

            # Skip "trivial" fractions and those we know won't simplify
            if nums[1] == 0 or denoms[1] == 0:
                continue

            # Is this a "curious" fraction?
            frac = Fraction(numerator, denominator)
            if ((nums[0] == denoms[1] and Fraction(nums[1], denoms[0]) == frac) or
                (nums[1] == denoms[0] and Fraction(nums[0], denoms[1]) == frac)):
                curious.append(frac)

    product = reduce(lambda a, b: a * b, curious, 1)
    print(f"Product: {product}")
    return

if __name__ == "__main__":
    main()
