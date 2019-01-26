import numpy as np

def main():
    """
    Entry point
    """
    s = ""
    i = 1
    while len(s) <= 1000000:
        s += str(i)
        i += 1
    
    total = np.prod([int(s[10 ** i - 1]) for i in range(7)])
    print(f"Product: {total}")

if __name__ == "__main__":
    main()
