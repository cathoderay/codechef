"""
  Url: https://www.codechef.com/problems/WEIRDO
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from collections import defaultdict
from sys import stdin, stdout
from math import log


is_vowel = lambda x: x in "aeiou"
cc = lambda s: not (is_vowel(s[0]) or is_vowel(s[1]))
cac = lambda s: not is_vowel(s[0]) and is_vowel(s[1]) and not is_vowel(s[2])


def is_alice(s):
    if cc(s[0:2]):
        return False

    for i in range(2, len(s)):
        if cc(s[i-1:i+1]) or cac(s[i-2:i+1]):
            return False
    return True


def accumulate(s, c, f, x):
    for i in s:
        c[i] += 1
        f[i] += 1

    for k in c.keys():
        x[k] += 1
    return f, x


def process(s, fA, xcA, fB, xcB, N):
    if is_alice(s):
        fA, xcA = accumulate(s, c, fA, xcA)
        N += 1
    else:
        fB, xcB = accumulate(s, c, fB, xcB)
    return fA, xcA, fB, xcB, N


def solve(L, N, fA, xcA, fB, xcB, sa, nsb, nsa):
    for i in xcA.keys():
        sa *= xcA[i]
        nsa *= fA[i]

    for i in xcB.keys():
        sa /= xcB[i]
        nsb *= fB[i]

    dn = M*log(nsb, 10) + 1
    dd = N*log(nsa, 10) + 1

    if dn > dd and (dn - dd) >= 10 and sa >= 1:
        return "Infinity"
   
    try:
        x = sa*(pow(nsb, M)/pow(nsa, N))
    except OverflowError:
        return "Infinity"

    return "Infinity" if x > 10000000 else str(x)


r = []
for _ in range(int(stdin.readline().strip())):
    L = int(stdin.readline().strip())
    N, M = 0, 0
    sa = nsb = nsa = 1
    xcA = defaultdict(int)
    xcB = defaultdict(int)
    fA = defaultdict(int)
    fB = defaultdict(int)

    for _ in range(L):
        s = stdin.readline().strip()
        c = defaultdict(int)
        fA, xcA, fB, xcB, N = process(s, fA, xcA, fB, xcB, N)
    M = L - N
    r.append(solve(L, N, fA, xcA, fB, xcB, sa, nsb, nsa))
stdout.write('\n'.join(r))
