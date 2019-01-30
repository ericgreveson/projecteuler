from digit_tools import from_digits, get_digits, num_digits

def search_permutations(cubes, n):
    """
    Search the (complete) list of cubes with the same amount of digits for n permutations
    Return a sorted list of these (smallest first) or None if n digit permutations don't exist
    """
    # First, transform the list into numbers with sorted digits
    cubes_digit_sorted = [from_digits(sorted(get_digits(c))) for c in cubes]

    # Now zip with the original cubes and sort smallest digit-sorted first
    zipped = sorted(zip(cubes, cubes_digit_sorted), key=lambda item: item[1])

    # And search for matches
    for index, (cube, digit_sorted) in enumerate(zipped[:-n]):
        matched_cubes = [cube]
        for i in range(1, n):
            if digit_sorted == zipped[index + i][1]:
                matched_cubes.append(zipped[index + i][0])

        if len(matched_cubes) == n:
            return sorted(matched_cubes)

    return None

def main():
    """
    Entry point
    """
    num_perms_to_find = 5

    # Start searching with the first 7 digit cube
    root = 100
    cubes = [100 ** 3]
    while True:
        root += 1
        cube = root ** 3
        if num_digits(cube) > num_digits(cubes[-1]):
            # Search the existing cube list for permutations
            result = search_permutations(cubes, num_perms_to_find)
            if result:
                break

            # Now clear the cube list and start on the new number of digits!
            cubes.clear()

        cubes.append(cube)

    print(f"Smallest cube with 5 digit perms: {result[0]} (permutations: {result})")

if __name__ == "__main__":
    main()
