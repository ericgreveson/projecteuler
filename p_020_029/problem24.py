import itertools

def main():
    """
    Entry point
    """
    # There are n! permutations of an n-item sequence
    for index, perms in enumerate(itertools.permutations(range(10))):
        if index == 999999:
            perm_str = "".join([str(i) for i in perms])
            print(f"Millionth permutation: {perm_str}")
            break
            
    return

if __name__ == "__main__":
    main()
