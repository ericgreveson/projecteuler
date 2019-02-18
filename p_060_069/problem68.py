from itertools import permutations

from digit_tools import from_digits

def is_magic_5gon_ring(elements):
    """
    Return True if elements (10-vector) form a "magic" ring
    """
    total = sum(elements[0:3])
    return sum(elements[2:5]) == total and sum(elements[4:7]) == total \
        and sum(elements[6:9]) == total and elements[1] + sum(elements[8:10]) == total

def to_digits(d):
    """
    Convert d to its digit array
    """
    if d == 10:
        return [1, 0]
    else:
        return [d]

def to_digit_list(p):
    """
    Convert permutation p to a digit list
    """
    d = [to_digits(value) for value in p]
    ordering = [0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1]
    result = []
    for index in ordering:
        result += d[index]

    return result

def main():
    """
    Entry point
    """
    # Figure out possible solutions with first clockwise node = 6
    # (highest possible: other external nodes are then 7, 8, 9, 10 in some order)
    # But can we make a "magic" one with first clockwise node = 6?
    # This one probably isn't magic but it's the best starting point, we can
    # count down from here
    best = 0
    for permutation in permutations(range(1, 11), 10):
        # First number can't be bigger than 6
        if permutation[0] > 6:
            continue

        # Must have 10 in external node, and all other externals must be greater than permutation[0]
        all_greater = True
        found_ten = False
        for i in [3, 5, 7, 9]:
            external_node = permutation[i]
            if external_node < permutation[0]:
                all_greater = False
                break

            if external_node == 10:
                found_ten = True

        if not (all_greater and found_ten):
            continue

        # Must be magic
        if is_magic_5gon_ring(permutation):
            # Convert to string
            digits = to_digit_list(permutation)
            best = max(from_digits(digits), best)

    print(f"Best: {best}")

if __name__ == "__main__":
    main()
