from digit_tools import is_palindrome

def main():
    """
    Entry point
    """
    palindromic = [i for i in range(1000000) if is_palindrome(i, 10) and is_palindrome(i, 2)]
    print(f"Sum: {sum(palindromic)}")

if __name__ == "__main__":
    main()
