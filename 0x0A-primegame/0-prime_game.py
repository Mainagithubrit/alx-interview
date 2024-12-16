#!/usr/bin/python3


def isWinner(x, nums):
    """A prime Game"""

    def sieve_of_eratosthenes(max_n):
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_n + 1, i):
                    primes[j] = False
        return primes

    # Precompute primes up to the maximum value in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Simulate each game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of prime numbers up to n
        prime_count = 0
        for i in range(1, n + 1):
            if primes[i]:
                prime_count += 1

        # If the number of primes is odd, Maria wins; if even, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
