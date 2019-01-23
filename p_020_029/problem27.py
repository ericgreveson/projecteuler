from factor_tools import is_prime

def main():
    """
    Entry point
    """
    # We consider quadratics of the form n^2 + an + b
    best = (0,)
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while True:
                x = n*n + a*n + b
                if not is_prime(x):
                    break
                
                n += 1

            if n > best[0]:
                best = (n, a, b)

    print(f"Longest sequence ({best[0]} steps) for a={best[1]}, b={best[2]}")
    print(f"Coeff product: {best[1]*best[2]}")

if __name__ == "__main__":
    main()
