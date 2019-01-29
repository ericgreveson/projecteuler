from digit_tools import is_palindrome, reverse_digits

def is_lychrel(n):
    """
    Is n a Lychrel number (defined as not becoming a palindrome
    after reversing and adding for 49 iterations)?
    """
    for _ in range(50):
        n = n + reverse_digits(n)
        if is_palindrome(n):
            return False

    return True

def main():
    """
    Entry point
    """
    lychrel = [i for i in range(1, 10000) if is_lychrel(i)]
    print(f"Number of Lychrels < 10000: {len(lychrel)}")

if __name__ == "__main__":
    main()
