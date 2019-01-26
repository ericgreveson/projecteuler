def is_palindrome(n, b):
    """
    Is the given number n a palindrome in base b?
    """
    if b == 10:
        n_str = str(n)
    elif b == 2:
        n_str = "{0:b}".format(n)
    else:
        raise RuntimeError("Only 2 and 10 bases supported")
    
    for i in range(len(n_str) // 2):
        if n_str[i] != n_str[-1 - i]:
            return False

    return True

def main():
    """
    Entry point
    """
    palindromic = [i for i in range(1000000) if is_palindrome(i, 10) and is_palindrome(i, 2)]
    print(f"Sum: {sum(palindromic)}")

if __name__ == "__main__":
    main()
