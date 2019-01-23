def load_input(filename):
    """
    Load input names from file
    """
    with open(filename) as f:
        return [quoted[1:-1] for quoted in f.readlines()[0].split(",")]

def name_value(name):
    """
    Compute name value for a name
    """
    return sum([ord(c) - ord('A') + 1 for c in name])

def main():
    """
    Entry point
    """
    names = sorted(load_input("problem22_input.txt"))
    all_name_scores = sum((index + 1) * name_value(name) for index, name in enumerate(names))
    print(f"Total: {all_name_scores}")
    return

if __name__ == "__main__":
    main()
