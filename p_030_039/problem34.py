import math

def sum_digits_factorial(n):
    """
    Compute sum of factorials of each digit in the number n
    """
    sum_fact = 0
    while n > 0:
        sum_fact += math.factorial(n % 10)
        n //= 10

    return sum_fact

def main():
    """
    Entry point
    """
    # Sum of all 9!'s is largest possible sum. 7*9! is a 7 digit number. 8*9! is still only 7 digits.
    largest = math.factorial(9) * 7
    curious = [i for i in range(10, largest) if sum_digits_factorial(i) == i]
    print(f"Sum of curious numbers: {sum(curious)} (numbers: {curious})")
    return

if __name__ == "__main__":
    main()
