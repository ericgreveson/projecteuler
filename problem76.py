def count_ways(target, max_integer=None, cache=None):
    """
    Count the number of ways of making target from sum of at least 1 integers
    with max_integer as the largest integer in the sum. If max_integer is not
    provided, count all possible ways from sum of at least 2 integers.
    """
    # Special cases: because we use this recursively, we'll special-case the 1 or 2 targets
    # and the 1 max_integer
    if max_integer == 1:
        return 1

    if target == 1:
        return 1
    elif target == 2 and max_integer == 2:
        return 2

    if not max_integer:
        max_integer = target - 1
    if max_integer > target:
        max_integer = target

    if not cache:
        # Create a cache for storing results for all combinations of (target, max_integer)
        cache = [[None] * target for i in range(target + 1)]
    elif cache[target][max_integer] is not None:
        return cache[target][max_integer]

    remainder = target
    ways = 0

    # How many ways are there to make target using max_integer at least once?
    while remainder > max_integer:
        remainder -= max_integer
        ways += count_ways(remainder, max_integer - 1, cache=cache)

    # Special case: we have just 1 way to make this last case!
    if remainder == max_integer:
        ways += 1

    # Now recurse with the next smaller max_integer
    if max_integer > 0:
        ways += count_ways(target, max_integer - 1, cache=cache)

    cache[target][max_integer] = ways
    return ways

def main():
    """
    Entry point
    """
    ways = count_ways(100)

    print(f"Ways: {ways}")

if __name__ == "__main__":
    main()
