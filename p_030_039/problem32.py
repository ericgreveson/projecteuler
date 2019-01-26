import math

from digit_tools import num_digits, test_pandigital_9
    
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
            if num_digits(a) + num_digits(b) + num_digits(product) > 9:
                break

            if test_pandigital_9(a, b, product):
                products.add(product)
    
    print(f"Sum of pandigital products: {sum(products)}")
    return

if __name__ == "__main__":
    main()
