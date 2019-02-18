def polygonal(i, n):
    """
    Compute i-polygonal number n
    For example, if i=3, the nth triangle number will be returned
    """
    return n * ((i - 2) * n + 4 - i) // 2

def chain_remaining_sets(first, prev, remaining_sets):
    """
    Search remaining_sets for candidates that can chain with prev, recursively,
    until all sets have been used to take exactly 1 candidate from
    first: if len(remaining_sets) == 1, we must close the chain with first two digits of first
    prev: must chain with last two digits of prev
    remaining_sets: the sets we can use to look for the next chain element
    return: None if there is no closed-loop chain, otherwise the array making the chain
    """
    new_prefix = prev % 100
    for index, candidate_set in enumerate(remaining_sets):
        for candidate in candidate_set:
            if candidate // 100 == new_prefix:
                # This could work. Check if it can form a chain
                if len(remaining_sets) == 1:
                    if candidate % 100 == first // 100:
                        # We found a chain!
                        return [candidate]
                else:
                    # Recurse to see if this candidate works out down the line
                    sub_chain = chain_remaining_sets(first, candidate, remaining_sets[:index] + remaining_sets[index+1:])
                    if sub_chain:
                        return [candidate] + sub_chain

    return None


def main():
    """
    Entry point
    """
    # Compute all 4-digit triangle, square, ... octagonal numbers
    poly = []
    for i in range(3, 9):
        four_digit_poly_i = []
        n = 1
        poly_i_n = 0
        while poly_i_n < 10000:
            poly_i_n = polygonal(i, n)
            if poly_i_n >= 1000:
                four_digit_poly_i.append(poly_i_n)

            n += 1

        poly.append(four_digit_poly_i)

    # Now search for a chain of six cyclic numbers, one from each polygonal order
    for first in poly[0]:
        # Which numbers could come next?
        valid_chain = chain_remaining_sets(first, first, poly[1:])
        if valid_chain:
            valid_chain = [first] + valid_chain
            break
        
    print(f"Chain: {valid_chain}, sum: {sum(valid_chain)}")

if __name__ == "__main__":
    main()
