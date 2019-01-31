import math

def root_as_continued_fraction(n):
    """
    Compute the sequence representing root(n) as continued fraction:
    root(n) = a0 + 1 / (a1 + 1 / (a2 + 1 / (a3 + 1 / (...))))
    return (first_coeff_seq, repeating_coeff_seq) where repeating_coeff_seq
    is an array that represents the periodic part that repeats forever.
    """
    # Get the integer part
    first_coeff = int(math.sqrt(n))
    coeffs = [first_coeff]

    # The rest is 1 / (1 / (root(n) - first_coeff)) == 1 / (a / (root(n) - b))
    a = 1
    b = first_coeff
    seq_markers = {}
    while True:
        # Now rearrange for the next one, a / (root(n) - b) such that the root is on top
        # To do this, multiply by (root(n) + b) to get:
        # a * (root(n) + b) / (n - b ** 2) == a * (root_n + b) / c
        c = n - b ** 2

        # Now rearrange a * (root_n + b) / c = d + (root_n + e) / f
        f = c // a
        d = int((math.sqrt(n) + b) / f)
        e = b - d * f

        # Have we seen this sequence marker before?
        seq_marker = (d, e, f)
        if seq_marker in seq_markers.keys():
            # Figure out the split-point for aperiodic and periodic parts
            index = seq_markers[seq_marker]
            return coeffs[:index], coeffs[index:]

        # Record the new coefficient and (d, e, f) sequence marker and update a, b
        seq_markers[seq_marker] = len(coeffs)
        coeffs.append(d)
        a = f
        b = -e
        