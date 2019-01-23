import math

def test_pandigital_9(*args):
    """
    Test if args together contain the digits 1 through 9 uniquely
    """
    digits = set()
    for a in args:
        while a > 0:
            digits.add(a % 10)
            a //= 10

    return len(digits) == 9 and 0 not in digits
    
def main():
    """
    Entry point
    """
    # Brute force: try all products to 10000x1000, skipping those when the digit total is too high
    products = set()
    for a in range(1, 1000):
        for b in range(a+1, 10000):
            # Stop this loop once we're getting too many digits
            product = a * b
            a_digits = 1 + int(math.log10(a))
            b_digits = 1 + int(math.log10(b))
            prod_digits = 1 + int(math.log10(product))
            if a_digits + b_digits + prod_digits > 9:
                break

            if test_pandigital_9(a, b, product):
                products.add(a*b)
    
    print(f"Sum of pandigital products: {sum(products)}")
    return

if __name__ == "__main__":
    main()
