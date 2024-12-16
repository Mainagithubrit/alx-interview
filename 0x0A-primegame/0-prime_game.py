#!/usr/bin/python3
""" A prime game"""


def isWinner(x, nums):
    """A game that checks for a number if is a prime number,
    The numbers to be checked are upto n, and if a number is selcted
    Its removed along with the numbers divisible by it"""

    def sieve_of_eratosthenes(max_n):
        """ A function that sieves through numbers"""
        if max_n < 2:
            return [False] * (max_n + 1)

        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_n + 1, i):
                    primes[j] = False
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = 0
        for i in range(1, n + 1):
            if primes[i]:
                prime_count += 1

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
