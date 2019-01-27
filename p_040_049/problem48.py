def main():
    """
    Entry point
    """
    sum_last_10_digits = 0
    for i in range(1, 1001):
        sum_last_10_digits += (i ** i) % (10 ** 10)

    print(f"Last 10 digits: {sum_last_10_digits % (10 ** 10)}")

if __name__ == "__main__":
    main()
