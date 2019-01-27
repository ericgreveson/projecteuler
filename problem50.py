from factor_tools import get_primes

def main():
    """
    Entry point
    """
    print("Get primes below one million...")
    primes = get_primes(1000000)
    prime_set = set(primes)

    # Now get the n-consecutive sums for each n-length starting from 6
    longest = None
    for n in range(6, len(primes)):
        # Initialize with sum of first n
        print(f"Try {n} consecutive primes...")
        consecutive_sums = [sum(primes[:n])]
        found_longest = False
        for i in range(1, len(primes) - n):
            # Can quickly compute the next one by adding the next prime and removing the previous first
            next_sum = consecutive_sums[-1] + primes[i + n - 1] - primes[i - 1]
            if next_sum > primes[-1]:
                # No point going any further for sequences of this length
                break
                
            if next_sum in prime_set:
                # We have a winner (for this length). On to the next length!
                print(f"Length = {n}, first = {primes[i]}, sum = {next_sum}")
                longest = next_sum
                found_longest = True
                break

            consecutive_sums.append(next_sum)

        if not found_longest and i == 1:
            # We grew too big on the first try. No more sequences to try
            break

    print(f"Longest: {longest}")

if __name__ == "__main__":
    main()
