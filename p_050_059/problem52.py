from digit_tools import get_digits, num_digits

def main():
    """
    Entry point
    """
    x = 1
    while True:
        nd_x = num_digits(x)
        d_x = sorted(get_digits(x))

        # Get multiples 2x, 3x... 6x
        wrong_num_digits = False
        all_permutations = True
        for multiplier in range(2, 7):
            y = multiplier * x

            # Does it have the same number of digits?
            nd_y = num_digits(y)
            if nd_y != nd_x:
                wrong_num_digits = True
                break

            # Is it a permutation of the digits of x?
            d_y = sorted(get_digits(y))
            if d_y != d_x:
                all_permutations = False
                break

        if wrong_num_digits:
            # No point continuing with any more x values with this number of digits
            x = 10 ** num_digits(x)
            continue

        if all_permutations:
            # Looking good!
            break

        x += 1

    print(f"First integer with 2-6x permutation multiples: {x}")

if __name__ == "__main__":
    main()
