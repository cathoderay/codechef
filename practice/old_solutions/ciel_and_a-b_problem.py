"""
 Problem: Ciel and A-B Problem 
 URL: http://www.codechef.com/problems/CIELAB
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


ab = input().split()
a, b = map(int, ab)

if b > a: a, b = b, a
n = a - b

st = str(n)
if int(st[len(st) - 1]) >= 3:
    print(n - 1)
else:
    print(n + 1)
