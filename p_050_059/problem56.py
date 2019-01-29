from digit_tools import get_digits

def main():
    """
    Entry point
    """
    digit_sums = [sum(get_digits(a ** b)) for a in range(1, 100) for b in range(1, 100)]
    print(f"Maximum digit sum: {max(digit_sums)}")

if __name__ == "__main__":
    main()
