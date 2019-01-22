def equals_sum_fifth_powers(x):
    """
    Return true if the number x equals the sum of its digits to the fifth power
    """
    digit_power_sum = 0
    digits_left = x
    while digits_left > 0:
        digit_power_sum += (digits_left % 10) ** 5
        digits_left //= 10

    return x == digit_power_sum

def main():
    """
    Entry point
    """
    results = [i for i in range(2, 1000000) if equals_sum_fifth_powers(i)]
    print(f"Total: {sum(results)} (values: {results})")
    return

if __name__ == "__main__":
    main()
