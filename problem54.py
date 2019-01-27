from collections import defaultdict

def load_input(filename):
    """
    Load poker hands from filename
    """
    hands = []
    with open(filename) as f:
        for line in f.readlines():
            tokens = line.strip().split(" ")
            cards = []
            for token in tokens:
                value = token[0]
                suit = token[1]
                if value == "A":
                    value = 14
                elif value == "K":
                    value = 13
                elif value == "Q":
                    value = 12
                elif value == "J":
                    value = 11
                elif value == "T":
                    value = 10
                else:
                    value = int(value)

                cards.append((value, suit))

            hands.append([cards[:5], cards[5:]])

    return hands

def take_highest_n_of_same_value(h, n):
    """
    Take n cards (e.g. 2 for a pair) of the same value from hand h (typically with 5 cards)
    If n == 2 and there are 2 pairs, return just the highest pair
    Raise ValueError if there aren't n matching cards
    Otherwise return (value of n cards, remainder)
    where remainder is a list of (value, suit) pairs containing the remaining cards
    """
    value_counts = defaultdict(int)
    for value, _ in h:
        value_counts[value] += 1

    # Find the best group
    best_group = 0
    for value, count in value_counts.items():
        if count == n and value > best_group:
            best_group = value

    if not best_group:
        raise ValueError()

    # Find remaining cards
    remainder = []
    for value, suit in h:
        if value != best_group:
            remainder.append((value, suit))

    return best_group, remainder

def has_pair(h):
    """
    One Pair: Two cards of the same value.
    Note that this function will return true even if there are two pair,
    full house, three pair, four of a kind and so on. So do those tests first.
    return: (hand value, remaining cards) or None
    """
    try:
        return take_highest_n_of_same_value(h, 2)
    except ValueError:
        return None
    
def has_two_pair(h):
    """
    Two Pairs: Two different pairs.
    return: (high pair value, remaining cards) or None
    In this case, remaining cards will have the lower pair value prepended with a suit of None
    """
    try:
        first_pair_value, remainder = take_highest_n_of_same_value(h, 2)
        second_pair_value, remainder = take_highest_n_of_same_value(remainder, 2)
        return first_pair_value, [(second_pair_value, None)] + remainder
    except ValueError:
        return None

def has_three_of_a_kind(h):
    """
    Three of a Kind: Three cards of the same value.
    return: (hand value, remaining cards) or None
    """
    try:
        return take_highest_n_of_same_value(h, 3)
    except ValueError:
        return None

def has_straight(h):
    """
    Straight: All cards are consecutive values.
    return: (hand value, remaining cards) or None
    """
    values = {value for value, _ in h}
    if len(values) == 5 and max(values) - min(values) == 4:
        return max(values), []
    else:
        return None

def has_flush(h):
    """
    Flush: All cards of the same suit.
    return: (hand value, remaining cards) or None
    """
    suits = {suit for _, suit in h}
    if len(suits) == 1:
        return max([value for value, _ in h]), []
    else:
        return None

def has_full_house(h):
    """
    Full House: Three of a kind and a pair.
    return: (hand value, remaining cards) or None
    In this case remaining cards will just contain a single element of (pair value, None)
    """
    try:
        three_value, remainder = take_highest_n_of_same_value(h, 3)
        pair_value, remainder = take_highest_n_of_same_value(remainder, 2)
        return three_value, [(pair_value, None)]
    except ValueError:
        return None

def has_four_of_a_kind(h):
    """
    Four of a Kind: Four cards of the same value.
    return: (hand value, remaining cards) or None
    """
    try:
        return take_highest_n_of_same_value(h, 4)
    except ValueError:
        return None

def has_straight_flush(h):
    """
    Straight Flush: All cards are consecutive values of same suit.
    return: (hand value, remaining cards) or None
    """
    if has_straight(h):
        return has_flush(h)

    return None

def has_royal_flush(h):
    """
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    return: (hand value, remaining cards) or None
    """
    result = has_straight_flush(h)
    if result and result[0] == 14:
        return result
    
    return None

def compute_hand_score(h):
    """
    Get the hand score of h as (rank, value, remainder)
    where rank is the hand rank (higher ranks are better)
    value is the card value within this rank
    remainder is the list of remaining cards, sorted highest first
    """
    tests = [has_royal_flush,
             has_straight_flush,
             has_four_of_a_kind,
             has_full_house,
             has_flush,
             has_straight,
             has_three_of_a_kind,
             has_two_pair,
             has_pair]
    
    for index, test in enumerate(tests):
        result = test(h)
        if result:
            rank = len(tests) - index
            return rank, result[0], sorted([value for value, _ in result[1]], reverse=True)

    # No test passed, so we only have high card
    values = [value for value, _ in h]
    high_value = max(values)
    return 0, high_value, sorted([value for value in values if value != high_value], reverse=True)

def first_hand_wins(h1, h2):
    """
    Return True if hand h1 beats hand h2
    """
    rank1, value1, remainder1 = compute_hand_score(h1)
    rank2, value2, remainder2 = compute_hand_score(h2)

    if rank1 != rank2:
        return rank1 > rank2

    if value1 != value2:
        return value1 > value2

    for v1, v2 in zip(remainder1, remainder2):
        if v1 != v2:
            return v1 > v2

    raise RuntimeError("Hands have equal value")

def main():
    """
    Entry point
    """
    hands = load_input("problem54_input.txt")
    player1_wins = 0
    for hand in hands:
        if first_hand_wins(hand[0], hand[1]):
            player1_wins += 1

    print(f"Player 1 wins {player1_wins} hands")

if __name__ == "__main__":
    main()
