from digit_tools import num_digits

def main():
    """
    Entry point
    """
    power = 1
    match_count = 0
    while True:
        # See how many positive integers have same digits as power
        i = 1
        while True:
            i_p = i ** power
            nd = num_digits(i_p)
            if nd == power:
                # Yep, this matches
                match_count += 1
            elif nd > power:
                # No more i values will have few enough digits
                break

            i += 1

        power += 1
        if num_digits(9 ** power) < power:
            # We're done
            break

    print(f"Number of digit-matched powers: {match_count}")

if __name__ == "__main__":
    main()
