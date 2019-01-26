def nth_pentagonal(n):
    """
    Compute the nth pentagonal number
    """
    return n * (3 * n - 1) // 2

def main():
    """
    Entry point
    """
    max_search = 100000
    pentagonal = [nth_pentagonal(n) for n in range(1, max_search + 1)]
    pent_set = set(pentagonal)
    best = None
    for delta in range(1, max_search):
        for i in range(max_search - delta):
            p1 = pentagonal[i]
            p2 = pentagonal[i + delta]
            dist = p2 - p1
            if best and dist > best[0]:
                # Distances are already bigger than best, we can stop checking here
                break

            if (p1 + p2) in pent_set and dist in pent_set:
                print(f"{p1}, {p2} (delta = {delta}) works both ways!")
                if not best or best[0] > dist:
                    best = (dist, p1, p2)

    if pentagonal[-1] - pentagonal[-2] <= best[0]:
        print(f"Need to check more! (last two: {pentagonal[-1]}, {pentagonal[-2]}) - increase max_search!")

    print(f"Best: D={best[0]}, p1={best[1]}, p2={best[2]}")

if __name__ == "__main__":
    main()
