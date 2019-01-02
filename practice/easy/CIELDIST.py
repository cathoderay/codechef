"""
  Url: https://www.codechef.com/problems/CIELDIST
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    v = list(map(int, input().strip().split()))
    v.sort()
    k = v[2] - v[1] - v[0]
    print(k if k > 0 else 0)
