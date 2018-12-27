"""
  Url: https://www.codechef.com/problems/LEDIV
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import gcd
from functools import reduce


def sieve_till(n):
    lim = int(n**0.5) + 2
    m = [True]*(n+1)
    primes = []
    #only need to go till the square root of n
    for i in range(2, lim):
        if m[i] == True:
            primes.append(i)
            # but I need to mark all of their multiples
            for j in range(i**2, n+1, i):
                m[j] = False
    #saving rest of non-marked primes
    for j in range(lim, n+1):
        if m[j] == True:
            primes.append(j)
    return primes


def factors(n, primes):
    factors = []
    square = n**0.5
    for i in primes:
        if i > square:
            break
        if n % i == 0:
            factors.append(i)
    if len(factors) == 0:
        factors = [n]
    return factors

primes = sieve_till(int((10**5)**0.5 + 1))

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
  
    X = reduce(gcd, A)
    f = factors(X, primes)
    if f[0] != 1:
        print(f[0])
    elif f[0] == 1 and len(f) > 1:
        print(f[1])
    else:
        print(-1)

