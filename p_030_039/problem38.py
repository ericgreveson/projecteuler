from digit_tools import num_digits, test_pandigital_9

def main():
    """
    Entry point
    """
    # We have been told that the largest pandigital must at least start with 9
    # and so we just need to try prefixes with 91 being our starting point!
    # The furthest we can conceivably go is a four-digit 9xxx times (1, 2)
    best_candidate = 918273645
    for start, end in [(91, 99), (912, 988), (9123, 9877)]:
        for i in range(start, end):
            prods = []
            num_digits_total = 0
            multiplier = 1
            while num_digits_total < 9:
                prod = i * multiplier
                prods.append(prod)
                num_digits_total += num_digits(prod)
                multiplier += 1

            if test_pandigital_9(*prods):
                new_candidate = 0
                for prod in prods:
                    new_candidate *= 10 ** num_digits(prod)
                    new_candidate += prod

                if new_candidate > best_candidate:
                    best_candidate = new_candidate

    print(f"Highest: {best_candidate}")

if __name__ == "__main__":
    main()
