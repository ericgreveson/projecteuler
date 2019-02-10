import math

from fraction_tools import root_as_continued_fraction

def main():
    """
    Entry point
    """
    periodic_parts = []
    for i in range(1, 10000):
        # Is root(i) irrational?
        root_i = math.sqrt(i)
        if int(root_i) == root_i:
            continue

        # Compute the aperiodic and periodic parts of the continued fraction form
        aperiodic, periodic = root_as_continued_fraction(i)
        if i == 23:
            print(f"{aperiodic} :: {periodic}")
        periodic_parts.append(periodic)

    num_odd = sum([1 for p in periodic_parts if len(p) % 2 == 1])
    print(f"Number of odd periodic parts: {num_odd}")

if __name__ == "__main__":
    main()
