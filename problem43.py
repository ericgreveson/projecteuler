import itertools

def main():
    """
    Entry point
    """
    division_tests = [2, 3, 5, 7, 11, 13, 17]
    results = []
    for perm in itertools.permutations(range(10), 10):
        n_str = "".join([str(p) for p in perm])
        ok = True
        for index, divisor in enumerate(division_tests):
            substr_i = int(n_str[index + 1:index + 4])
            if substr_i % divisor != 0:
                ok = False
                break

        if ok:
            # All divisor substring tests passed!
            results.append(int(n_str))

    print(f"Sum: {sum(results)}")

if __name__ == "__main__":
    main()
