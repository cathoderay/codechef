"""
  Url: https://www.codechef.com/problems/EARTSEQ
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def sieve_till(n):
    lim = int(n**0.5) + 2
    m = [True]*(n+1)
    primes = []
    for i in range(2, lim):
        if m[i] == True:
            primes.append(i)
            for j in range(i**2, n+1, i):
                m[j] = False
    for j in range(lim, n+1):
        if m[j] == True:
            primes.append(j)
    return primes


primes = sieve_till(10**6)


for _ in range(int(input())):
    N = int(input())
   
    x = [6, 10, 15]
    if N % 3 == 0:
        r = [6, 10, 15]
    elif N % 3 == 1:
        r = [21, 14, 10, 15] 
    else:
        r = [33, 77, 14, 10, 15]

    for i in range(N - 3 - N % 3):
        r.append(x[i % 3]*primes[i+5])
        
    print(' '.join(map(str, r)))
