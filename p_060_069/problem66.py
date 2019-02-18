from collections import deque
import math

from fraction_tools import root_as_continued_fraction

def is_square(n):
    """
    Is n (>=1) a square number?
    """
    return int(math.sqrt(n)) ** 2 == n
    
def min_x_diophantine(d):
    """
    Find the minimum solution for x^2 - d * y^2 = 1, with x, y integers
    """
    # This is a Pell equation, apparently. And you can find a solution by
    # looking at the continued fraction for root(d)
    aperiodic, periodic = root_as_continued_fraction(d)
    coeffs = aperiodic + periodic
    hs = [1, coeffs[0]]
    ks = [0, 1]

    # Do the aperiodic parts first, then keep looping the periodic parts
    h = 0
    k = 0
    coeff_queue = deque(coeffs[1:])
    while h*h - d*k*k != 1:
        # If the queue's empty, refill it from the periodic sequence
        if not coeff_queue:
            coeff_queue = deque(periodic)

        # Get the next coefficient
        coeff = coeff_queue.popleft()
        h = coeff * hs[-1] + hs[-2]
        k = coeff * ks[-1] + ks[-2]

        # Is this a solution?
        if h*h - d*k*k == 1:
            break

        hs.append(h)
        ks.append(k)

    return h

def main():
    """
    Entry point
    """
    min_x_solutions = [(d, min_x_diophantine(d)) for d in range(1, 1001) if not is_square(d)]
    largest_solution = max(min_x_solutions, key=lambda item: item[1])
    print(f"Max x found when d = {largest_solution[0]} (x = {largest_solution[1]})")

if __name__ == "__main__":
    main()
