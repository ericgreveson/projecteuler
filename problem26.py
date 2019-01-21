def compute_cycle_length_with_denom(denom):
    """
    Compute the decimal cycle length for unit fraction 1/denom (where denom>1)
    e.g. 1/6 has decimal representation 0.1(6) so cycle length is 1, etc
    """
    digit_pos = 0

    # Remaining fraction after subtracting away portions of earlier decimal digits
    frac_numer = 1
    frac_numer_history = dict()
    while True:
        digit_pos += 1

        # For this digit position, compute the common denominator and numerator
        # for the remaining fraction. E.g. if we started with denom = 7, then:
        # digit_pos=1: frac = 1/7   => 10/70 - 1*7/70 = 3/70        [0.1]
        # digit_pos=2: frac = 3/70  => 30/700 - 4*7/700 = 2/700     [0.14]
        # digit_pos=3: frac = 2/700 => 20/7000 - 2*7/7000 = 6/7000  [0.142]

        # It's clear that we can ignore the denominator (it's known from digit_pos):
        # digit_pos=4: frac = 6/d  => 60/10d - 8*7/10d = 4/10d      [0.1428]
        # digit_pos=5: frac = 4/d  => 40/10d - 5*7/10d = 5/10d      [0.14285]
        # digit_pos=6: frac = 5/d  => 50/10d - 7*7/10d = 1/10d      [0.142857]
        # digit_pos=7: frac = 1/d  => we're back to digit_pos=1! Seq length is 7-1 = 6.

        # Another example for 1/6:
        # digit_pos=1: frac = 1/d  => 10/10d - 1*6/10d = 4/10d      [0.1]
        # digit_pos=2: frac = 4/d  => 40/10d - 6*6/10d = 4/10d      [0.16]
        # digit_pos=3: frac = 4/d  => we're back to digit_pos=2! Seq length is 3-2 = 1.
        minuend = 10 * frac_numer
        subtrahend = denom
        digit = minuend // subtrahend
        difference = minuend - digit * subtrahend

        # Has it terminated?
        if difference == 0:
            return 0

        # Have we found a repeating sequence?
        if frac_numer in frac_numer_history:
            return digit_pos - frac_numer_history[frac_numer]

        # Add this digit to the "seen before" dict
        frac_numer_history[frac_numer] = digit_pos

        # Update remaining fraction numerator
        frac_numer = difference


def main():
    """
    Entry point
    """
    longest_cycle = 0
    longest_cycle_denom = 0
    for i in range(2, 1000):
        cycle_length = compute_cycle_length_with_denom(i)
        if cycle_length > longest_cycle:
            longest_cycle = cycle_length
            longest_cycle_denom = i

    print(f"Longest cycle is {longest_cycle} for d={longest_cycle_denom}")
    return

if __name__ == "__main__":
    main()
