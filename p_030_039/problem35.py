from collections import deque
from factor_tools import is_prime
    
def is_circular_prime(n):
    """
    Return true if all rotations of digits of n are prime
    """
    # Single-digit numbers: easy
    if n < 10:
        return is_prime(n)
        
    # Multi-digit numbers: stick in a deque for easy rotation
    digits = deque()
    while n > 0:
        # If a digit is even, or 5, or 0, at least one rotation won't be prime
        digit = n % 10
        if digit == 0 or digit == 5 or digit % 2 == 0:
            return False

        digits.appendleft(digit)
        n //= 10

    for _ in range(len(digits)):
        candidate = 0
        multiplier = 1
        for d in digits:
            candidate += d * multiplier
            multiplier *= 10

        if not is_prime(candidate):
            return False

        digits.rotate()

    return True

def main():
    """
    Entry point
    """
    circ_primes = [i for i in range(2, 1000000) if is_circular_prime(i)]
    print(f"Number of circular primes: {len(circ_primes)}")

if __name__ == "__main__":
    main()
