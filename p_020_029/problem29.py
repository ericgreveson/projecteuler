def main():
    """
    Entry point
    """
    # Compute all combinations and stick in a list
    powers = [a ** b for a in range(2, 101) for b in range(2, 101)]
    distinct = set(powers)
    print(f"Distinct items: {len(distinct)}")
    return

if __name__ == "__main__":
    main()
