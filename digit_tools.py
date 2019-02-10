import math

def num_digits(n):
    """
    Return the number of digits (in base 10) for integer n > 0
    """
    return int(math.log10(n)) + 1

def get_digits(n):
    """
    Get the array of digits for n
    """
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10

    return digits

def from_digits(digits):
    """
    Make a number from its digit array (inverse of get_digits)
    """
    n = 0
    multiplier = 1
    for d in reversed(digits):
        n += multiplier * d
        multiplier *= 10

    return n

def reverse_digits(n):
    """
    Reverse the digits of n
    """
    multiplier = 10 ** (num_digits(n) - 1)
    reversed_n = 0
    while n > 0:
        reversed_n += (n % 10) * multiplier
        multiplier //= 10
        n //= 10

    return reversed_n

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

def is_palindrome(n, base=10):
    """
    Is the given number n a palindrome in the given base?
    """
    if base == 10:
        n_str = str(n)
    elif base == 2:
        n_str = "{0:b}".format(n)
    else:
        raise RuntimeError("Only 2 and 10 bases supported")
    
    for i in range(len(n_str) // 2):
        if n_str[i] != n_str[-1 - i]:
            return False

    return True

def concatenate_digits(a, b):
    """
    Concatenate the digits of a and b
    e.g. a=42, b=666 returns 42666
    """
    return a * (10 ** num_digits(b)) + b
    
def is_permutation(a, b):
    """
    Test if the digits of a are a permutation of the digits of b
    """
    digits_a = sorted(get_digits(a))
    digits_b = sorted(get_digits(b))
    if len(digits_a) != len(digits_b):
        return False

    for da, db in zip(digits_a, digits_b):
        if da != db:
            return False

    return True
    