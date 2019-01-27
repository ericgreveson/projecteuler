def load_input(filename):
    """
    Load input file
    """
    with open(filename) as f:
        return [word[1:-1] for word in "".join(f.readlines()).strip().split(",")]

def nth_triangle_number(n):
    """
    Compute the nth triangle number
    """
    return n * (n + 1) // 2

def word_value(word):
    """
    Compute the value of word
    """
    return sum([ord(c) - ord('A') + 1 for c in word])

def main():
    """
    Entry point
    """
    words = load_input("problem42_input.txt")
    values = [word_value(word) for word in words]
    max_value = max(values)
    triangle_numbers = {1}
    n = 2
    last_triangle_number = 1
    while last_triangle_number < max_value:
        last_triangle_number = nth_triangle_number(n)
        triangle_numbers.add(last_triangle_number)
        n += 1

    num_triangle_words = sum([1 if value in triangle_numbers else 0 for value in values])
    print(f"Num triangle words: {num_triangle_words}")

if __name__ == "__main__":
    main()
