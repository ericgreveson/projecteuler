from math import factorial

def main():
    """
    Entry point
    """
    # Prepare factorials for O(1) lookup
    factorials = [1]
    for i in range(1, 101):
        factorials.append(factorials[-1] * i)

    # Now start counting
    ncr_count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            ncr = factorials[n] / (factorials[r] * factorials[n - r])
            if ncr > 1000000:
                ncr_count += 1

    print(f"Count: {ncr_count}")
    
if __name__ == "__main__":
    main()
