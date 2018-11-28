"""
  Url: https://www.codechef.com/problems/PRIME1
"""

from math import sqrt


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


MAXN = 10**9+1
lim = int(sqrt(MAXN)+1) + 1


def sieve(lim):
    ns = [0]*(lim+2)
    primes = []
    for i in range(2, lim+2):
        if ns[i] == 0:
            primes.append(i)
            for j in range(2*i, lim+2, i):
                ns[j] = 1
    return primes

primes = sieve(lim)

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    sq = sqrt(n) + 1
    for f in primes:
        if f > sq:
            return True
        if n % f == 0:
            return False
    return True


for _ in range(int(input())):
    m, n = list(map(int, input().split()))
    for i in range(m, n + 1):
        if is_prime(i):
            print(i)
    print()
