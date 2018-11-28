"""
  Url: https://www.codechef.com/problems/BUYING2
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, X = list(map(int, input().split()))

    ns = list(map(int, input().split()))

    SUM = sum(ns) 
    if SUM % X >= min(ns):
        print(-1)
    else:
        print(SUM//X)


