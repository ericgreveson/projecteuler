from factor_tools import is_prime

def is_right_truncatable_prime(p):
    """
    Is the prime p still prime for all right truncations?
    """
    truncated = p // 10
    while truncated > 0:
        if not is_prime(truncated):
            return False

        truncated //= 10

    return True

def is_left_truncatable_prime(p):
    """
    Is the prime p still prime for all left truncations?
    """
    truncate_modulo = 10
    truncated = p % truncate_modulo
    while truncated != p:
        if not is_prime(truncated):
            return False

        truncate_modulo *= 10
        truncated = p % truncate_modulo

    return True

def main():
    """
    Entry point
    """
    truncatable = []
    i = 10
    while len(truncatable) < 11:
        i += 1
        if is_prime(i) and is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            truncatable.append(i)

    print(f"Sum: {sum(truncatable)}")

if __name__ == "__main__":
    main()
