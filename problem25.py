def main():
    """
    Entry point
    """
    # Get computing Fibonacci numbers
    index = 3
    f_minus_2 = 1
    f_minus_1 = 1
    f = 2
    while f < 10 ** 999:
        f_minus_2 = f_minus_1
        f_minus_1 = f
        f = f_minus_1 + f_minus_2
        index += 1

    print(f"Index: {index}, F: {f}")
    
if __name__ == "__main__":
    main()
