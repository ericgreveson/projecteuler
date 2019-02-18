from math import factorial

from digit_tools import get_digits

def nonrepeating_chain_length(n):
    """
    Compute the length of the nonrepeating part for digit-wise factorial summation
    """
    visited = set()
    while n not in visited:
        visited.add(n)
        n = sum([factorial(d) for d in get_digits(n)])

    return len(visited)

def main():
    """
    Entry point
    """
    sixty_length = [i for i in range(1, 1000000) if nonrepeating_chain_length(i) == 60]
    print(f"There are {len(sixty_length)} 60-long nonrepeating chains")

if __name__ == "__main__":
    main()
