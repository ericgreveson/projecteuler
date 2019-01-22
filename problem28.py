def compute_spiral_diagonal_sum(first_elem, loop_wh):
    """
    Compute the sum of the four diagonal elements for the given loop
    first_elem: First element (in the right-most, second-down element of this loop)
    loop_wh: Width / height of the spiral's loop to compute the diag-sum
    return: sum of the four diagonal elements
    """
    lower_right = first_elem + loop_wh - 2
    return 4 * lower_right + 6 * loop_wh - 6

def main():
    """
    Entry point
    """
    # Count the central "1" as a special case
    sum_diagonals = 1

    # Now proceed on the 3-length, 5-length etc loops
    start_elem = 2
    for loop_wh in range(3, 1002, 2):
        sum_diagonals += compute_spiral_diagonal_sum(start_elem, loop_wh)
        start_elem += loop_wh ** 2 - (loop_wh - 2) ** 2

    print(f"Sum: {sum_diagonals}")
    return

if __name__ == "__main__":
    main()
