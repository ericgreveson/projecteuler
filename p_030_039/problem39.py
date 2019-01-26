from collections import defaultdict
import math

def main():
    """
    Entry point
    """
    p_map = defaultdict(list)
    for a in range(1, 1000):
        for b in range(1, 1000):
            c_float = math.sqrt(a*a + b*b)
            c = int(c_float)
            if c_float == c:
                # We have a right angled triangle. What's the perimeter?
                p = a + b + c
                if p > 1000:
                    # We can stop searching this b range now
                    break

                p_map[p].append((a, b))

    max_p, solutions = max(p_map.items(), key=lambda item: len(item[1]))
    print(f"Most solutions for p={max_p} (with {len(solutions)} solutions)")

if __name__ == "__main__":
    main()
