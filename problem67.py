import math

def load_input(filename):
    """
    Get the input triangle as a list of lists
    """
    with open(filename) as f:
        triangle_text = f.readlines()
        return [[int(x) for x in row.strip().split(" ")] for row in triangle_text]

def find_max_path(triangle):
    """
    Find maximum-sum path from top of triangle to bottom
    """
    # Start by copying the values
    sums = [[x for x in row] for row in triangle]
    # Efficient algorithm: start at the bottom and work our way up, computing max sums
    for reverse_index, row in enumerate(reversed(sums)):
        if reverse_index == 0:
            # Easy: max value for subpaths from last row is cell value itself
            continue

        # Now we need to take sum of each cell and max of two subpaths
        row_below = sums[-reverse_index]
        for col_index, col in enumerate(row):
            left = row_below[col_index]
            right = row_below[col_index + 1]
            row[col_index] = col + max(left, right)
            
    return sums[0][0]

def main():
    """
    Entry point
    """
    # Brute force it for now
    triangle = load_input("problem67_input.txt")
    best_total = find_max_path(triangle)
    print(f"Best total: {best_total}")
    return

if __name__ == "__main__":
    main()