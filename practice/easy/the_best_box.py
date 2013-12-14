"""
 Problem: The best box 
 URL: http://www.codechef.com/problems/J7
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


import math

for t in range(int(input())):
    p, s = map(int, input().split())
    x = (-p/2.0 + math.sqrt(p*p/4.0 - 6.0*s))/-6.0
    z = p/4.0 - 2*x
    print(round(x*x*z, 2))
