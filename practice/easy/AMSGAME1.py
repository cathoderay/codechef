"""
  Url: https://www.codechef.com/problems/AMSGAME1
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"



from math import gcd
from functools import reduce


for _ in range(int(input())):
    N = int(input())    
    ns = list(map(int, input().split()))

    print(reduce(gcd, ns))



