"""
 Problem: Nuclear Reactors
 URL: http://www.codechef.com/problems/NUKES
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def basen(number, base, k):
    s = []
    for i in range(k):
       s.append(str(number % base))
       number = int(number/base)
    print ' '.join(s)

a, n, k = (int(i) for i in raw_input().split())

basen(a, n+1, k)
