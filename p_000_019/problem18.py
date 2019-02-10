
class Triangle:
    def __init__(self):
        """
        Get the input triangle as a list of lists
        """
        triangle_text = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
        self._rows = [[int(x) for x in row.split(" ")] for row in triangle_text.splitlines()]
        self._sums = [[0 for x in row] for row in self._rows]

    def max_of_subpaths(self, r, c):
        """
        Find the maximum sum over all subpaths
        r: row to start on
        c: column to start on within row
        return: max sum from all subpaths (including the start node)
        """
        if r >= len(self._rows):
            return 0

        # There are two subpaths: "left" and "right". Try both of them.
        left = self.max_of_subpaths(r+1, c)
        right = self.max_of_subpaths(r+1, c+1)
        self._sums[r][c] = self._rows[r][c] + max(left, right)
        return self._rows[r][c] + max(left, right)

def main():
    """
    Entry point
    """
    # Brute force it for now
    triangle = Triangle()
    best_total = triangle.max_of_subpaths(0, 0)

    for row in triangle._sums:
        for x in row:
            print(f"{x:4} ", end='')
        print()

    print(f"Best total: {best_total}")
    return

if __name__ == "__main__":
    main()