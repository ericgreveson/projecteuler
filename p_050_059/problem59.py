def load_input(filename):
    """
    Load input ciphertext
    """
    with open(filename) as f:
        return [int(token) for token in f.readlines()[0].strip().split(",")]

def xor_decode(ciphertext, key):
    """
    Decode some ciphertext with the given key with XOR algorithm
    ciphertext: the ciphertext to decode (as a string)
    key: the key to use (array of ints representing ASCII codes)
    """
    return "".join([chr(c ^ key[index % len(key)]) for index, c in enumerate(ciphertext)])

def main():
    """
    Entry point
    """
    ciphertext = load_input("problem59_input.txt")
    
    # Try three-letter combos and work out which looks like English
    likely_key = None
    for i in range(ord("a"), ord("z")+1):
        for j in range(ord("a"), ord("z")+1):
            for k in range(ord("a"), ord("z")+1):
                key = [i, j, k]
                decoded_fragment = xor_decode(ciphertext, key)
                key_str = "".join([chr(c) for c in key])
                if "the" in set(decoded_fragment.split(" ")):
                    likely_key = key
                    print(f"Likely key '{key_str}': {decoded_fragment}")

    decoded = [ord(c) for c in xor_decode(ciphertext, likely_key)]
    print(f"Sum of decoded ASCII values: {sum(decoded)}")

if __name__ == "__main__":
    main()
