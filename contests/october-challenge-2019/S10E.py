"""
  Url: https://www.codechef.com/problems/S10E
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import inf 


for _ in range(int(input())):
    _ = int(input())
    P = map(int, input().split())
    c, l = 0, [inf]
    for p in P:
        if p < min(l): c += 1
        if len(l) == 5: l.pop(0) 
        l.append(p)
    print(c)

