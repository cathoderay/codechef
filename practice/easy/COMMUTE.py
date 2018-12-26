"""
  Url: https://www.codechef.com/problems/COMMUTE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import ceil


for _ in range(int(input())):
    n = int(input())
    t = 0
    for i in range(1, n + 1):
        x, l, f = list(map(int, input().split())) 
        if t <= x:
            t = x
        elif t > x:
            t = x + ceil((t-x)/f)*f 
        t += l
    print(t)
