"""
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
"""

def isPrime(num, primes):
    if num in primes:
        return True
    for prime in list(primes):
        if num % prime == 0:
            return False
    return True

def findPrimes(num):

    candidates = []
    primes = set()
    for i in range(2, num//2+1):
        if isPrime(i, primes):
            primes.add(i)
            candidates.append((i, num-i))

    new_candidates = []
    for first, second in candidates:
        if isPrime(second, primes):
            primes.add(second)
            new_candidates.append((first, second))

    return new_candidates[0]

if __name__ == '__main__':

    assert findPrimes(4) == (2,2)
    assert findPrimes(10) == (3,7)
    assert findPrimes(100) == (3,97)

