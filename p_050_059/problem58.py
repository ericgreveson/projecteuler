from factor_tools import is_prime

def main():
    """
    Entry point
    """
    num_prime = 3
    num_on_diagonals = 1 + 4
    size = 3
    while num_prime / num_on_diagonals > 0.1:
        size += 2
        bottom_right = size * size
        other_diags = [bottom_right - i * (size - 1) for i in range(1, 4)]
        num_prime += sum([1 for i in other_diags if is_prime(i)])
        num_on_diagonals += 4

    print(f"Side length with <10% prime along diag: {size}")

if __name__ == "__main__":
    main()
