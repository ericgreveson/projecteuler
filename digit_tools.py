import math

def get_digits(n):
    """
    Get the array of digits for n
    """
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10

    return digits

def test_pandigital_9(*args):
    """
    Test if args together contain the digits 1 through 9 uniquely
    """
    digits = set()
    digit_count = 0
    for a in args:
        while a > 0:
            digits.add(a % 10)
            digit_count += 1
            a //= 10

    return digit_count == 9 and len(digits) == 9 and 0 not in digits
    
def num_digits(n):
    """
    Return the number of digits (in base 10) for integer n > 0
    """
    return int(math.log10(n)) + 1
    