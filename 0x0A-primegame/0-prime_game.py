def sieve_of_eratosthenes(max_n):
    """
    Generate a list where primes[i] is True if i is a prime number.
    """
    if max_n < 2:  # If max_n is 0 or 1, there are no prime numbers
        return [False] * (max_n + 1)

    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:  # If i is still prime
            for j in range(i * i, max_n + 1, i):
                primes[j] = False  # Mark multiples of i as not prime

    return primes


def isWinner(x, nums):
    """
    Determine the winner of the prime game based on x rounds and nums.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the player who won the most rounds, or None if it's a tie.
    """
    if x == 0 or not nums:  # No rounds to play or empty input
        return None

    max_n = max(nums)  # Find the largest number in nums
    if max_n < 2:  # No prime numbers if all nums are <= 1
        return None

    # Generate a sieve for prime numbers up to max_n
    primes = sieve_of_eratosthenes(max_n)

    # Keep track of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:  # Skip invalid rounds where n <= 1
            ben_wins += 1
            continue

        # Count the total prime numbers up to n
        prime_count = sum(primes[:n + 1])

        # Ben wins if the count is odd, Maria wins if even
        if prime_count % 2 == 1:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
