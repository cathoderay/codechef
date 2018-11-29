
"""
  Url: https://www.codechef.com/problems/DIVIDING
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


n = int(input())
ns = list(map(int, input().split()))

if sum(ns) == (n*(n+1))/2:
    print("YES")
else:
    print("NO")
