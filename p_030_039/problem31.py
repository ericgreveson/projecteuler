class CoinArray(list):
    """
    Coin list that is hashable for storage in sets
    The 8 entries are [1p count, 2p count, 5p count, ... , 200p count]
    """
    def __hash__(self):
        """
        Hash this as a string
        """
        return hash(" ".join([str(i) for i in self]))

def main():
    """
    Entry point
    """
    # Important: sorted smallest to largest
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coin_index = {coin: index for index, coin in enumerate(coins)}
    
    # How many ways are there of making each number from 1 to 200 from these values?
    # Building up from 1 means we can re-use earlier results
    # e.g.:
    # 1p: [{1}]
    # 2p: [{1,1}, {2}]
    # 3p: [{1,1,1}, {2,1}]
    # 4p: [{1,1,1,1}, {2,1,1}, {2,2}]
    # etc
    way_sets = [None]
    for i in range(1, 201):
        way_set_i = set()

        # Try using 1 of each coin and then all the ways of the remainder, if > 0
        for coin in coins:
            remainder = i - coin

            if remainder == 0:
                # We can make this with exactly this coin alone - but no larger coins
                coin_count = [0 for i in coins]
                coin_count[coin_index[coin]] = 1
                way_set_i.add(CoinArray(coin_count))
                break
            elif remainder > 0:
                # We can use this coin and whatever the options for the smaller value are
                for rem_list in way_sets[remainder]:
                    new_coin_count = [c for c in rem_list]
                    new_coin_count[coin_index[coin]] += 1
                    way_set_i.add(CoinArray(new_coin_count))
            else:
                # Can't use any bigger coins
                break

        way_sets.append(way_set_i)

    print(f"Number of ways of making £2: {len(way_sets[200])}")
    return

if __name__ == "__main__":
    main()
